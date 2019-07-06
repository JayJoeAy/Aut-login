from webbot import Browser 
web = Browser()
web.go_to('https://login.aut.ac.ir/login') 
web.type('m_erfan_hamdi' , into='username')
web.type('25HK884V5' , into='password')
web.click('ورود')
#web.click('NEXT' , tag='span')
#web.type('mypassword' , into='Password' , id='passwordFieldId') # specific selection
#web.click('NEXT' , tag='span') # you are logged in ^_^