 s=smtplib.SMTP('smtp.gmail.com',587)
    
    s.ehlo()
    
    s.starttls()
    
    s.login('boiii2412@gmail.com','motorcop')
    
    subject = 'Autoroad - Booking Confirmation '
    body = 'HEY',FULLNAME,'!!,You have booked a', CARNAME ,'from ',PICKDATE,'to',DROPDATE,',.This is to inform you that your booking is CONFIRMED' 
    
    message = f'Subject : {subject}\n\n {body}'
    
    s.sendmail('boiii2412@gmail.com',EMAIL,message)
    
    print ('HEY AN EMAIL HAS BEEN SENT!')
    
    s.quit()