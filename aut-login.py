from webbot import Browser 
web = Browser()
web.go_to('https://internet.aut.ac.ir/') 
web.type('user' , into='username') #enter your username here !
web.type('pass' , into='password') #Enter your password here !
web.click('ورود')
