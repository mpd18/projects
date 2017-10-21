Import-Module PSSQLite
$db = "C:\Users\Michael\Documents\Powershell\LastIssue.db"
$dateQuery = "SELECT date FROM Hajime_Issues ORDER BY date DESC LIMIT 1"
$insertQuery = "INSERT INTO Hajime_Issues (title,link,date) VALUES ("
$lastDate = Invoke-SqliteQuery -Query $dateQuery -DataSource $db -As "SingleValue"
$string = ""
$xml = [xml](Invoke-WebRequest -Uri "https://www.mangastream.com/rss")
$content = $xml.rss.channel.item
forEach($item in $content)
{
    if($item.title -like 'Hajime*')
    {
        if([datetime]$item.pubDate -gt [datetime]$lastDate)
        {
            $string += $item.title + "`n" + $item.pubDate + "`n" + $item.link + "`n`n"
            $insertQuery += "'" + $item.title + "','" + $item.link + "','" + $item.pubDate + "');"
            Invoke-SqliteQuery -Query $insertQuery -DataSource $db
        }
        $insertQuery = "INSERT INTO Hajime_Issues (title,link,date) VALUES ("
    }
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