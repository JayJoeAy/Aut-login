from webbot import Browser 
web = Browser()
web.go_to('https://internet.aut.ac.ir/') 
web.type('put your username here' , into='username') #enter your username here !
web.type('put your password here' , into='password') #Enter your password here !
web.click('ورود')
