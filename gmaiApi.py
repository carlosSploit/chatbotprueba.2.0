import smtplib

messeg = "Contenedor de messeg"
nombre = "contenedor de nombre"

email = """From: %s
To: %s
MIME-Version: 1.0
Content-type: text/html
Subject: %s

%s
"""


def htmldataresult(mes, nom, numero, correo):

    global contentmesseg
    global nombre
    global messeg
    messeg = mes + 'te puedes contactar conmigo : ' + \
        correo + ' y mi numeor de telefono es : ' + numero
    nombre = nom

    contentmesseg = """<!doctype html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml"
    xmlns:o="urn:schemas-microsoft-com:office:office">

<head>
    <title>

    </title>
    <!--[if !mso]><!-- -->
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <!--<![endif]-->
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cssarch.herokuapp.com/css/link.css" rel="stylesheet" type="text/css">
    <!--[if !mso]><!-->
    <link href="https://cssarch.herokuapp.com/css/link2.css" rel="stylesheet" type="text/css">
    <!--<![endif]-->
    <!--[if mso]>
        <xml>
        <o:OfficeDocumentSettings>
          <o:AllowPNG/>
          <o:PixelsPerInch>96</o:PixelsPerInch>
        </o:OfficeDocumentSettings>
        </xml>
        <![endif]-->
    <!--[if lte mso 11]>
        <style type="text/css">
          .outlook-group-fix { width:100% !important; }
        </style>
        <![endif]-->
    <!--[if !mso]><!-->
    <link href="https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Cabin:400,700" rel="stylesheet" type="text/css">
    <!--<![endif]-->
    <link href="https://cssarch.herokuapp.com/css/link3.css" rel="stylesheet" type="text/css">
    <link href="https://cssarch.herokuapp.com/css/link4.css" rel="stylesheet" type="text/css">
    <link href="https://cssarch.herokuapp.com/css/link5.css" rel="stylesheet" type="text/css">
    <link href="https://cssarch.herokuapp.com/css/link6.css" rel="stylesheet" type="text/css">
</head>

<body style="background-color:#FFFFFF;">
    <div style="background-color:#FFFFFF;">
        <table align="center"
            background="https://storage.googleapis.com/topolio25132/plugin-assets/6320/25132/Gijonresized-scaled%20edited_91b3f2c7-794f-4e57-bcb2-a862a06b94f0.png"
            border="0" cellpadding="0" cellspacing="0" role="presentation"
            style="background:#fc5c04 url(https://storage.googleapis.com/topolio25132/plugin-assets/6320/25132/Gijonresized-scaled%20edited_91b3f2c7-794f-4e57-bcb2-a862a06b94f0.png) top center / cover repeat;width:100%;">
            <tbody>
                <tr>
                    <td>
                        <!--[if mso | IE]>
        <v:rect  style="mso-width-percent:1000;" xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false">
        <v:fill  origin="0.5, 0" position="0.5, 0" src="https://storage.googleapis.com/topolio25132/plugin-assets/6320/25132/Gijonresized-scaled%20edited_91b3f2c7-794f-4e57-bcb2-a862a06b94f0.png" color="#fc5c04" type="tile" />
        <v:textbox style="mso-fit-shape-to-text:true" inset="0,0,0,0">

      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->
                        <div style="Margin:0px auto;max-width:600px;">
                            <div style="line-height:0;font-size:0;">
                                <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation"
                                    style="width:100%;">
                                    <tbody>
                                        <tr>
                                            <td
                                                style="direction:ltr;font-size:0px;padding:28px 0px 28px 0px;text-align:center;vertical-align:top;">
                                                <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
        <tr>
            <td
               class="" style="vertical-align:top;width:600px;"
            >
          <![endif]-->
                                                <div class="mj-column-per-100 outlook-group-fix"
                                                    style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                                    <table border="0" cellpadding="0" cellspacing="0"
                                                        role="presentation" style="vertical-align:top;" width="100%">
                                                        <tr>
                                                            <td align="center"
                                                                style="font-size:0px;padding:0px 0px 0px 0px;word-break:break-word;">
                                                                <table border="0" cellpadding="0" cellspacing="0"
                                                                    role="presentation"
                                                                    style="border-collapse:collapse;border-spacing:0px;">
                                                                    <tbody>
                                                                        <tr>
                                                                            <td style="width:372px;">
                                                                                <img height="auto"
                                                                                    src="https://storage.googleapis.com/topolio25132/plugin-assets/6320/25132/vector.png"
                                                                                    style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;"
                                                                                    width="372">
                                                                            </td>
                                                                        </tr>
                                                                    </tbody>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </div>

                                                <!--[if mso | IE]>
            </td>
        </tr>
                  </table>
                <![endif]-->
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                        <!--[if mso | IE]>
          </td>
        </tr>
      </table>
        </v:textbox>
      </v:rect>
    <![endif]-->
                    </td>
                </tr>
            </tbody>
        </table>
        <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
            <tbody>
                <tr>
                    <td>
                        <!--[if mso | IE]>
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->
                        <div style="Margin:0px auto;max-width:600px;">
                            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation"
                                style="width:100%;">
                                <tbody>
                                    <tr>
                                        <td
                                            style="direction:ltr;font-size:0px;padding:9px 0px 9px 0px;text-align:center;vertical-align:top;">
                                            <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
        <tr>
            <td
               class="" style="vertical-align:top;width:600px;"
            >
          <![endif]-->
                                            <div class="mj-column-per-100 outlook-group-fix"
                                                style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                                <table border="0" cellpadding="0" cellspacing="0" role="presentation"
                                                    style="vertical-align:top;" width="100%">
                                                    <tr>
                                                        <td align="left"
                                                            style="font-size:0px;padding:15px 15px 15px 15px;word-break:break-word;">

                                                            <div
                                                                style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:11px;line-height:1.5;text-align:left;color:#000000;">
                                                                <p style="text-align: center;"><span
                                                                        style="font-size: 24px; font-family: Arial, sans-serif;"><strong> """ + nombre + """</strong></span>
                                                                </p>
                                                            </div>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td
                                                            style="font-size:0px;padding:10px 10px;padding-top:10px;word-break:break-word;">
                                                            <p
                                                                style="border-top:solid 1px #000000;font-size:1;margin:0px auto;width:100%;">
                                                            </p>
                                                            <!--[if mso | IE]>
        <table
           align="center" border="0" cellpadding="0" cellspacing="0" style="border-top:solid 1px #000000;font-size:1;margin:0px auto;width:580px;" role="presentation" width="580px"
        >
          <tr>
            <td style="height:0;line-height:0;">
              &nbsp;
            </td>
          </tr>
        </table>
      <![endif]-->
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td align="left"
                                                            style="font-size:0px;padding:15px 15px 15px 15px;word-break:break-word;">
                                                            <div
                                                                style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:11px;line-height:1.5;text-align:left;color:#000000;">
                                                                <p style="text-align: center;"><span
                                                                        style="font-size: 17px; font-family: Arial, sans-serif;"> """ + messeg + """ </span>
                                                                </p>
                                                            </div>
                                                        </td>
                                                    </tr>
                                                </table>
                                            </div>
                                            <!--[if mso | IE]>
            </td>
        </tr>
                  </table>
                <![endif]-->
                                        </td>
                                    </tr>
                                </tbody>
                            </table>

                        </div>
                        <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      <![endif]-->
                    </td>
                </tr>
            </tbody>
        </table>
        <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation"
            style="background:#0c84fc;background-color:#0c84fc;width:100%;">
            <tbody>
                <tr>
                    <td>
                        <!--[if mso | IE]>
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->
                        <div style="Margin:0px auto;max-width:600px;">
                            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation"
                                style="width:100%;">
                                <tbody>
                                    <tr>
                                        <td
                                            style="direction:ltr;font-size:0px;padding:9px 0px 9px 0px;text-align:center;vertical-align:top;">
                                            <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
        <tr>
            <td
               class="" style="width:600px;"
            >
          <![endif]-->
                                            <div class="mj-column-per-100 outlook-group-fix"
                                                style="font-size:0;line-height:0;text-align:left;display:inline-block;width:100%;direction:ltr;">
                                                <!--[if mso | IE]>
        <table  role="presentation" border="0" cellpadding="0" cellspacing="0">
          <tr>
              <td
                 style="vertical-align:top;width:600px;"
              >
              <![endif]-->
                                                <div class="mj-column-per-100 outlook-group-fix"
                                                    style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                                    <table border="0" cellpadding="0" cellspacing="0"
                                                        role="presentation" style="vertical-align:top;" width="100%">
                                                        <tr>
                                                            <td align="center"
                                                                style="font-size:0px;padding:10px 10px 10px 10px;word-break:break-word;">
                                                                <!--[if mso | IE]>
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" role="presentation"
      >
        <tr>
              <td>
            <![endif]-->
                                                                <table align="center" border="0" cellpadding="0"
                                                                    cellspacing="0" role="presentation"
                                                                    style="float:none;display:inline-table;">
                                                                    <tr>
                                                                        <td style="padding:4px;">
                                                                            <table border="0" cellpadding="0"
                                                                                cellspacing="0" role="presentation"
                                                                                style="background:transparent;border-radius:3px;width:35px;">
                                                                                <tr>
                                                                                    <td
                                                                                        style="font-size:0;height:35px;vertical-align:middle;width:35px;">
                                                                                        <a href="https://fb.me/Casas360.org"
                                                                                            target="_blank"
                                                                                            style="color: #0000EE;">
                                                                                            <img alt="facebook"
                                                                                                height="35"
                                                                                                src="https://s3-eu-west-1.amazonaws.com/ecomail-assets/editor/social-icos/roundedwhite/facebook.png"
                                                                                                style="border-radius:3px;display:block;"
                                                                                                width="35">
                                                                                        </a>
                                                                                    </td>
                                                                                </tr>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </table>
                                                                <!--[if mso | IE]>
              </td>
              <td>
            <![endif]-->
                                                                <table align="center" border="0" cellpadding="0"
                                                                    cellspacing="0" role="presentation"
                                                                    style="float:none;display:inline-table;">
                                                                    <tr>
                                                                        <td style="padding:4px;">
                                                                            <table border="0" cellpadding="0"
                                                                                cellspacing="0" role="presentation"
                                                                                style="background:transparent;border-radius:3px;width:35px;">
                                                                                <tr>
                                                                                    <td
                                                                                        style="font-size:0;height:35px;vertical-align:middle;width:35px;">
                                                                                        <a href="https://mobile.twitter.com/Casas360_org"
                                                                                            target="_blank"
                                                                                            style="color: #0000EE;">
                                                                                            <img alt="twitter"
                                                                                                height="35"
                                                                                                src="https://s3-eu-west-1.amazonaws.com/ecomail-assets/editor/social-icos/roundedwhite/twitter.png"
                                                                                                style="border-radius:3px;display:block;"
                                                                                                width="35">
                                                                                        </a>
                                                                                    </td>
                                                                                </tr>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </table>
                                                                <!--[if mso | IE]>
              </td>

              <td>
            <![endif]-->
                                                                <table align="center" border="0" cellpadding="0"
                                                                    cellspacing="0" role="presentation"
                                                                    style="float:none;display:inline-table;">
                                                                    <tr>
                                                                        <td style="padding:4px;">
                                                                            <table border="0" cellpadding="0"
                                                                                cellspacing="0" role="presentation"
                                                                                style="background:transparent;border-radius:3px;width:35px;">
                                                                                <tr>
                                                                                    <td
                                                                                        style="font-size:0;height:35px;vertical-align:middle;width:35px;">
                                                                                        <a href="https://www.linkedin.com/PROFILE"
                                                                                            target="_blank"
                                                                                            style="color: #0000EE;">
                                                                                            <img alt="linkedin"
                                                                                                height="35"
                                                                                                src="https://s3-eu-west-1.amazonaws.com/ecomail-assets/editor/social-icos/roundedwhite/linkedin.png"
                                                                                                style="border-radius:3px;display:block;"
                                                                                                width="35">
                                                                                        </a>
                                                                                    </td>
                                                                                </tr>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </table>
                                                                <!--[if mso | IE]>
              </td>
              <td>
            <![endif]-->
                                                                <table align="center" border="0" cellpadding="0"
                                                                    cellspacing="0" role="presentation"
                                                                    style="float:none;display:inline-table;">
                                                                    <tr>
                                                                        <td style="padding:4px;">
                                                                            <table border="0" cellpadding="0"
                                                                                cellspacing="0" role="presentation"
                                                                                style="background:transparent;border-radius:3px;width:35px;">
                                                                                <tr>
                                                                                    <td
                                                                                        style="font-size:0;height:35px;vertical-align:middle;width:35px;">
                                                                                        <a href="https://www.instagram.com/Casas360_org/"
                                                                                            target="_blank"
                                                                                            style="color: #0000EE;">
                                                                                            <img alt="instagram"
                                                                                                height="35"
                                                                                                src="https://s3-eu-west-1.amazonaws.com/ecomail-assets/editor/social-icos/roundedwhite/instagram.png"
                                                                                                style="border-radius:3px;display:block;"
                                                                                                width="35">
                                                                                        </a>
                                                                                    </td>
                                                                                </tr>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </table>
                                                                <!--[if mso | IE]>
              </td>

          </tr>
        </table>
      <![endif]-->


                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td
                                                                style="font-size:0px;padding:10px 10px;padding-top:10px;word-break:break-word;">
                                                                <p
                                                                    style="border-top:solid 1px #FFFEFE;font-size:1;margin:0px auto;width:100%;">
                                                                </p>
                                                                <!--[if mso | IE]>
        <table
           align="center" border="0" cellpadding="0" cellspacing="0" style="border-top:solid 1px #FFFEFE;font-size:1;margin:0px auto;width:580px;" role="presentation" width="580px"
        >
          <tr>
            <td style="height:0;line-height:0;">
              &nbsp;
            </td>
          </tr>
        </table>
      <![endif]-->
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td align="left"
                                                                style="font-size:0px;padding:15px 15px 15px 15px;word-break:break-word;">
                                                                <div
                                                                    style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:11px;line-height:1.5;text-align:left;color:#000000;">
                                                                    <p style="text-align: center;"><span
                                                                            style="font-family: Arial, sans-serif;"><strong><span
                                                                                    style="color: #ecf0f1; font-size: 13px;">Central:
                                                                                    &nbsp; +51
                                                                                    984129585</span></strong></span></p>
                                                                    <p style="text-align: center;"><span
                                                                            style="font-family: Arial, sans-serif;"><strong><span
                                                                                    style="color: #ecf0f1; font-size: 13px;">Lunes
                                                                                    a Viernes de 09:00 am a 06:00
                                                                                    pm</span></strong></span></p>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </div>
                                                <!--[if mso | IE]>
              </td>

          </tr>
          </table>
        <![endif]-->
                                            </div>
                                            <!--[if mso | IE]>
            </td>
        </tr>

                  </table>
                <![endif]-->
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      <![endif]-->
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</body>

</html>

"""
    return contentmesseg


def Mandandomesseg(messeg, nombre, numero, correo):
    mensaje = htmldataresult(messeg, nombre, numero, correo)
    global email
    # edtmessegnfcod
    # edtnombrenfcod

    # remplazar con los datos
    remitente = "server <arturo14212000@gmail.com>"
    destinatario = "Empresa <arturo14212000@gmail.com>"
    asunto = 'Consulta en mensaje'
    email = email % (remitente, destinatario, asunto, mensaje)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login('arturo14212000@gmail.com', '@123456789987654321')

    server.sendmail(remitente,  # emisor
                    destinatario,  # reseptor
                    email)  # messeg
    server.close()


# htmldataresult()
# Mandandomesseg('quiero comerme un culo de locos',
#               'carlos arturo guerrero castillo', '969280255', 'arturo14212000@gmail.com')
