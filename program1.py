import pandas as pd
import textwrap

file_path = 'data.xlsx'
sheet_name = 'Sheet1'
df = pd.read_excel('C:/Ayip/dokumwn w p e/SEMESTER 2/STRUKTUR DATA/UTS/data.xlsx')
df = df.astype(str)
df.fillna('', inplace=True)
df['NIM'] = df['NIM'].astype(str)
df['Nama Mahasiswa'] = df['Nama Mahasiswa'].astype(str)
df['Sumber Database'] = df['Sumber Database'].astype(str)
df['Judul Paper'] = df['Judul Paper'].astype(str)
df['Tahun Terbit'] = df['Tahun Terbit'].astype(str)
df['Abstrak (langusung copas dari paper)'] = df['Abstrak (langusung copas dari paper)'].astype(str)
df['Nama Penulis'] = df['Nama Penulis'].astype(str)


print("\n=========BERIKUT ADALAH DATA YANG DIAMBIL SEBAGIAN DARI DATABASE==========\n")
print(df[['NIM', 'Nama Mahasiswa', 'Sumber Database', 'Judul Paper', 'Tahun Terbit']].head(10))
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None) 

df[['NIM', 'Nama Mahasiswa', 'Sumber Database', 'Judul Paper', 'Tahun Terbit', 'Abstrak (langusung copas dari paper)','Kesimpulan (Langusung copas dari paper)','Link Paper', 'Nama Penulis' ]].head(3493)

while True:
    print("\n===============================MENU pilihan===============================\n")
    print("1. search linear")
    print("2. search binary")
    print("3. keluar")
    pilih = input("Masukkan pilihan anda: ")
    if pilih== '1':
        while True:
            print("\n===================================MENU pilihan=====================================\n")
            print("1. Cari berdasarkan NIM, Nama Mahasiswa, Sumber Database, Nama Penulis, Tahun Terbit")
            print("2. Menampilkan abstrak dan kesimpulan dari judul paper")
            print("3. keluar")
            pilihan = input("Masukkan pilihan anda: ")

            if pilihan == '1':
                keyword=input("Masukkan kata kunci untuk mencari data\n(NIM, Nama Mahasiswa, Sumber Database, Nama Penulis, Tahun Terbit): ")
                
                hasil = []
                for index, row in df.iterrows():
                    if keyword.lower() in str(row['NIM']).lower() or keyword.lower() in str(row['Nama Mahasiswa']).lower() or keyword.lower() in str(row['Nama Penulis']).lower() or keyword.lower() in str(row['Sumber Database']).lower() or keyword.lower() in str(row['Judul Paper']).lower() or keyword.lower() in str(row['Tahun Terbit']).lower():
                        hasil.append(row)
                hasil_cari = pd.DataFrame(hasil)
                if not hasil_cari.empty:
                    print("\n=================================HASIL PENCARIAN=================================\n")
                    for index, item in hasil_cari.iterrows():
                        tahun = item['Tahun Terbit']
                        print("NIM            : ", item['NIM'])
                        print("Nama Mahasiswa : ", item['Nama Mahasiswa'])
                        print("Sumber Database: ", item['Sumber Database'])
                        print("nama penulis   : ", item['Nama Penulis'])
                        print("Judul Paper    : ", item['Judul Paper'])

                        if tahun.strip() == '' or tahun.lower() == 'nan':
                            print("Tahun Terbit   : Tidak tersedia")
                        else:
                            print("Tahun Terbit   : ", int(float(tahun)))

                        print("--------------------------------------------------")
                else:
                    print("Data tidak ditemukan.")
            elif pilihan == '2':
                judul = input("Masukkan judul paper: ")
                hasil = []
                for index, row in df.iterrows():
                    if judul.lower() in str(row['Judul Paper']).lower():
                        hasil.append(row)
                hasil_cari = pd.DataFrame(hasil)
                if not hasil_cari.empty:
                    print("\n================================HASIL PENCARIAN================================\n")
                    for index, item in hasil_cari.iterrows():
                        avstrak = textwrap.fill(item['Abstrak (langusung copas dari paper)'], width=120)
                        kesimpulan = textwrap.fill(item['Kesimpulan (Langusung copas dari paper)'], width=120)
                        link = textwrap.fill(item['Link Paper'], width=120)
                        tahun = item['Tahun Terbit']
                  
                        print("NIM            : ", item['NIM'])
                        print("Nama Mahasiswa : ", item['Nama Mahasiswa'])
                        print("Sumber Database: ", item['Sumber Database'])
                        print("Nama Penulis   : ", item['Nama Penulis'])
                        print("Judul Paper    : ", item['Judul Paper'])

                        if tahun.strip() == '' or tahun.lower() == 'nan':
                            print("Tahun Terbit   : Tidak tersedia")
                        else:
                            print("Tahun Terbit   : ", int(float(tahun)))

                        print("Abstrak        :\n", avstrak)
                        print("Kesimpulan     :\n", kesimpulan)
                        print("Link Paper     : ", link)
                        print("--------------------------------------------------")
                else:
                    print("Data tidak ditemukan.")

            elif pilihan == '3':
                print("Terima kasih telah menggunakan program ini.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
    elif pilih == '2':
        while True:
            print("\n===================================MENU pilihan====================================\n")
            print("1. Cari berdasarkan NIM, Nama Mahasiswa, Sumber Database, Tahun Terbit")
            print("2. Menampilkan abstrak dan kesimpulan dari judul paper")
            print("3. keluar")
            pilihan2 = input("Masukkan pilihan anda: ")
            if pilihan2 == '1':
                while True:
                    print("\n===================================MENU pilihan====================================\n")
                    pilihan3 = input("Pilih metode pencarian:\n1. Mencari berdasarkan NIM\n2. Mencari berdasarkan Nama Mahasiswa\n3. Mencari berdasarkan Sumber Database\n4. Mencari berdasarkan Tahun Terbit\n5. Mencari berdasarkan Nama penulis\n6. Keluar\nMasukkan pilihan anda: ")
                    if pilihan3 == '1':
                        keyword = input("NIM: ")
                        df_sorted = df.sort_values(by='NIM').reset_index(drop=True)
                        low = 0
                        high = len(df_sorted) - 1
                        while low <= high:
                                mid = (low + high) // 2
                                mid_nim = df_sorted.loc[mid, 'NIM']
                                if mid_nim == keyword:
                                    print("\n================================HASIL PENCARIAN================================\n")
                                    print("NIM            : ", df_sorted.loc[mid, 'NIM'])
                                    print("Nama Mahasiswa : ", df_sorted.loc[mid, 'Nama Mahasiswa'])
                                    print("Sumber Database: ", df_sorted.loc[mid, 'Sumber Database'])
                                    print("Nama Penulis   : ", df_sorted.loc[mid, 'Nama Penulis'])
                                    print("Judul Paper    : ", df_sorted.loc[mid, 'Judul Paper'])
                                    print("Tahun Terbit   : ", str(df_sorted.loc[mid, 'Tahun Terbit']).replace('.0', ''))
                                    print("--------------------------------------------------")
                                    break
                                elif mid_nim < keyword:
                                    low = mid + 1
                                else:
                                    high = mid - 1
                        else:
                            print("Data tidak ditemukan.")
                            break
                    elif pilihan3 == '2':
                        keyword = input("Nama Mahasiswa: ")
                        df_sorted = df.sort_values(by='Nama Mahasiswa').reset_index(drop=True)
                        low = 0
                        high = len(df_sorted) - 1
                        while low <= high:
                                mid = (low + high) // 2
                                mid_nama = df_sorted.loc[mid, 'Nama Mahasiswa']
                                if mid_nama == keyword:
                                    print("\n================================HASIL PENCARIAN================================\n")
                                    print("NIM            : ", df_sorted.loc[mid, 'NIM'])
                                    print("Nama Mahasiswa : ", df_sorted.loc[mid, 'Nama Mahasiswa'])
                                    print("Sumber Database: ", df_sorted.loc[mid, 'Sumber Database'])
                                    print("Nama Penulis   : ", df_sorted.loc[mid, 'Nama Penulis'])
                                    print("Judul Paper    : ", df_sorted.loc[mid, 'Judul Paper'])
                                    print("Tahun Terbit   : ", str(df_sorted.loc[mid, 'Tahun Terbit']).replace('.0', ''))
                                    print("--------------------------------------------------")
                                    break
                                elif mid_nama < keyword:
                                    low = mid + 1
                                else:
                                    high = mid - 1
                        else:
                            print("Data tidak ditemukan.")
                            break
                    elif pilihan3 == '3':   
                        keyword = input("Sumber Database: ")
                        df_sorted = df.sort_values(by='Sumber Database').reset_index(drop=True)
                        low = 0
                        high = len(df_sorted) - 1
                        while low <= high:
                                mid = (low + high) // 2
                                mid_sumber = df_sorted.loc[mid, 'Sumber Database']
                                if mid_sumber == keyword:
                                    print("\n================================HASIL PENCARIAN================================\n")
                                    print("NIM            : ", df_sorted.loc[mid, 'NIM'])
                                    print("Nama Mahasiswa : ", df_sorted.loc[mid, 'Nama Mahasiswa'])
                                    print("Sumber Database: ", df_sorted.loc[mid, 'Sumber Database'])
                                    print("Nama Penulis   : ", df_sorted.loc[mid, 'Nama Penulis'])
                                    print("Judul Paper    : ", df_sorted.loc[mid, 'Judul Paper'])
                                    print("Tahun Terbit   : ", str(df_sorted.loc[mid, 'Tahun Terbit']).replace('.0', ''))
                                    print("--------------------------------------------------")
                                    break
                                elif mid_sumber < keyword:
                                    low = mid + 1
                                else:
                                    high = mid - 1
                        else:
                            print("Data tidak ditemukan.")
                            break
                    
                    elif pilihan3 == '4':
                        try:
                            keyword = int(input("Tahun Terbit: "))
                        except ValueError:
                            print("Input harus berupa angka tahun (contoh: 2007)")
                            continue
                        df_sorted = df.sort_values(by='Tahun Terbit').reset_index(drop=True)
                        low = 0
                        high = len(df_sorted) - 1
                        while low <= high:
                                mid = (low + high) // 2
                                mid_tahun = int(float(df_sorted.loc[mid, 'Tahun Terbit']))
                                if mid_tahun == keyword:
                                    print("\n================================HASIL PENCARIAN================================\n")
                                    print("NIM            : ", df_sorted.loc[mid, 'NIM'])
                                    print("Nama Mahasiswa : ", df_sorted.loc[mid, 'Nama Mahasiswa'])
                                    print("Sumber Database: ", df_sorted.loc[mid, 'Sumber Database'])
                                    print("Nama Penulis   : ", df_sorted.loc[mid, 'Nama Penulis'])
                                    print("Judul Paper    : ", df_sorted.loc[mid, 'Judul Paper'])
                                    print("Tahun Terbit   : ", mid_tahun)
                                    print("--------------------------------------------------")
                                    break
                                elif mid_tahun < keyword:
                                    low = mid + 1
                                else:
                                    high = mid - 1
                        else:
                            print("Data tidak ditemukan.")
                            break
                    elif pilihan3 == '5':
                        keyword = input("Nama penulis: ")
                        df_sorted = df.sort_values(by='Nama Penulis').reset_index(drop=True)
                        low = 0
                        high = len(df_sorted) - 1
                        while low <= high:
                                mid = (low + high) // 2
                                mid_penulis = df_sorted.loc[mid, 'Nama Penulis']
                                if mid_penulis == keyword:
                                    print("\n================================HASIL PENCARIAN================================\n")
                                    print("NIM            : ", df_sorted.loc[mid, 'NIM'])
                                    print("Nama Mahasiswa : ", df_sorted.loc[mid, 'Nama Mahasiswa'])
                                    print("Sumber Database: ", df_sorted.loc[mid, 'Sumber Database'])
                                    print("Nama Penulis   : ", df_sorted.loc[mid, 'Nama Penulis'])
                                    print("Judul Paper    : ", df_sorted.loc[mid, 'Judul Paper'])
                                    print("Tahun Terbit   : ", str(df_sorted.loc[mid, 'Tahun Terbit']).replace('.0', ''))
                                    print("--------------------------------------------------")
                                    break
                                elif mid_penulis < keyword:
                                    low = mid + 1
                                else:
                                    high = mid - 1
                        else:
                            print("Data tidak ditemukan.")
                            break
                    elif pilihan3 == '6':
                        print('keluar')
                        break  
                    else:
                        print("Data tidak ditemukan.")
            elif pilihan2 == '2':
                keyword = input("Masukkan judul paper: ")
                df_sorted = df.sort_values(by='Judul Paper').reset_index(drop=True)
                low = 0
                high = len(df_sorted) - 1
                while low <= high:
                    mid = (low + high) // 2
                    mid_judul = df_sorted.loc[mid, 'Judul Paper']
                    if mid_judul == keyword:
                        print("\n================================HASIL PENCARIAN================================\n")
                        avstrak = textwrap.fill(df_sorted.loc[mid, 'Abstrak (langusung copas dari paper)'], width=120)
                        kesimpulan = textwrap.fill(df_sorted.loc[mid, 'Kesimpulan (Langusung copas dari paper)'], width=120)
                        link = textwrap.fill(df_sorted.loc[mid, 'Link Paper'], width=120)
                        print("NIM            : ", df_sorted.loc[mid, 'NIM'])
                        print("Nama Mahasiswa : ", df_sorted.loc[mid, 'Nama Mahasiswa'])
                        print("Sumber Database: ", df_sorted.loc[mid, 'Sumber Database'])
                        print("Nama Penulis   : ", df_sorted.loc[mid, 'Nama Penulis'])
                        print("Judul Paper    : ", df_sorted.loc[mid, 'Judul Paper'])
                        print("Tahun Terbit   : ", str(df_sorted.loc[mid, 'Tahun Terbit']).replace('.0', ''))
                        print("Abstrak        :\n", avstrak)
                        print("Kesimpulan     :\n",kesimpulan)
                        print("Link Paper     : ",link)
                        print("--------------------------------------------------")
                        break
                    elif mid_judul < keyword:
                        low = mid + 1
                    else:
                        high = mid - 1
                else:
                    print("Data tidak ditemukan.")
            elif pilihan2 == '3':
                print("Terima kasih telah menggunakan program ini.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    elif pilih == '3':
        while True:
            print("Terima kasih telah menggunakan program ini.")
            break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        