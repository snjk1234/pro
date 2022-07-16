from mailer import Mailer

mail = Mailer(email='omarassir22@gmail.com',
              password='abcdef2030')

mail.send(receiver='omarassir12@gmail.com',  # Email From Any service Provider
          #no_reply='noreplay@example.com', # Redirect receiver to another email when try to reply.
          subject='TEST',
          message='HI, This Message From Python :)')