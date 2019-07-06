from webbot import Browser 
web = Browser()
web.go_to('https://internet.aut.ac.ir/') 
web.type('m_erfan_hamdi' , into='username') #enter your username here !
web.type('25HK884V5' , into='password') #Enter your password here !
web.click('ورود')
