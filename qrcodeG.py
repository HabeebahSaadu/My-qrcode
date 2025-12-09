import qrcode
def generate_qrcode(txt):
    qr= qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 12,
        border = 4
    )

    qr.add_data(txt)
    qr.make(fit = True)
    img = qr.make_image(fill_color = "Black", black_color = "white")
    img.save("facebook.png")
generate_qrcode("https://web.facebook.com/?ref=homescreenpwa&_rdc=1&_rdr#")