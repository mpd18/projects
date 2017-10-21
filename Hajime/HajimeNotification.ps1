Import-Module PSSQLite
$db = 'C:\Users\Michael\Documents\Code\PowerShell\Hajime\LastIssue.db'
$dateQuery = "SELECT date FROM Hajime_Issues ORDER BY date DESC LIMIT 1"
$insertQuery = "INSERT INTO Hajime_Issues (title,link,date) VALUES ("
$lastDate = Invoke-SqliteQuery -Query $dateQuery -DataSource $db -As "SingleValue"
$string = ""
$xml = [xml](Invoke-WebRequest -Uri "https://www.mangastream.com/rss")
$content = $xml.rss.channel.item
$string=""
forEach($item in $content) {
    if(($item.title -like 'Hajime*') -and ([datetime]$item.pubDate -gt [datetime]$lastDate)) {
        $string += $item.title + "`n" + $item.pubDate + "`n" + $item.link + "`n`n"
        $insertQuery += "'" + $item.title + "','" + $item.link + "',CURRENT_TIMESTAMP);"
        Invoke-SqliteQuery -Query $insertQuery -DataSource $db
    }
    $insertQuery = "INSERT INTO Hajime_Issues (title,link,date) VALUES ("
}
$params = @{
    From="Hajime@hajime.com"
    To="michaeldeanxc@gmail.com"
    Body=$string
    Subject="Hajime update"
    Smtpserver= "aspmx.l.google.com"
}
if($string -ne "")
{
    Send-MailMessage @params
}