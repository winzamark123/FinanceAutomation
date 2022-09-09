import pdftables_api

c = pdftables_api.Client('zu9hzrgc0b3u')
c.csv('RyderPayment_Sep22.pdf', 'RyderPayment_Sep22') 
#replace c.xlsx with c.csv to convert to CSV
#replace c.xlsx with c.xml to convert to XML
#replace c.xlsx with c.html to convert to HTML