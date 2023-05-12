import numpy as np #Mengimport library numpy kemudian di inisialisasi dengan np
import imageio # Mengimport library dari imageio
import cv2 as cv #Memasukan atau mengimport library dari cv2
import matplotlib.pyplot as plt #Mengimport pyplot dari matplotlib kemudian di inisialisasi dengan plt


img = cv.imread(r"C:\Users\ASUS\Documents\FILE SYAHDAN\semester 6\PCD\PRAKTIKUM 5\Saitama.JPG")#Membaca gambar format JPEG dengan kode cv dan disimpan dalam variabel img



#Mendapatkan/define resolusi dan tipe gambar
img_height = img.shape[0]#Tinggi gambar disimpan pada variabel img.shape 0
img_width = img.shape[1]#Panjang gambar disimpan pada variabel img.shape 1
img_channel = img.shape[2]# Warna Channel gambar disimpan pada variabel img.shape 2
img_type = img.dtype#Mendapatkan tipe data dan membuat variabel img_type


img_brightness = np.zeros(img.shape, dtype = np.uint8)# digunakan untuk membuat array berukuran sama dengan gambar asli, dengan nilai awal 0 dan tipe data unsigned integer 8 bit


#Membuat fungsi menghitung nilai brighter
def brighter(nilai):
    for y in range(0, img_height):#Pengunlangan iterasi y pada variabel img_height
        for x in range(0, img_width):#Pengunlangan iterasi x pada variabel img_width
            red = img[y][x][0]##Mendapatkan itensitas warna merah
            green = img[y][x][1]#Mendapatkan itensitas warna hijau
            blue = img[y][x][2]#Mendapatkan itensitas warna biru
            gray = (int(red) + int(green) + int(blue))/3
            gray += nilai#Mengisi array pada variabel gray dengan 1 (hanya ada satu piksel)
            if gray > 255: 
                gray = 255 #jika gray lebih dari 255 maka akan sama dengan 255 
            if gray < 0:
                gray = 0 #jika gray kurang dari 0 maka akan sama degan 0
            img_brightness[y][x] = (gray, gray, gray)#Hanya menghasilkan piksel warna abu-abu

#Menampilkan gambar dengan parameter -100
brighter(-100)
cv.imshow('Brightness -100',img_brightness)#Memunculkan gambar dari variabel img_brightness dan memberi judul
cv.waitKey(0)#Tampilan akan menutup dengan bebas menekan tombol tanpa batas waktu
cv.destroyAllWindows()#digunakan untuk menutup seluruh jendela

brighter(25)
cv.imshow('Brightness +25',img_brightness)#Memunculkan gambar dari variabel img_brightness dan memberi judul
cv.waitKey(0)#Tampilan akan menutup dengan bebas menekan tombol tanpa batas wakt
cv.destroyAllWindows()

#brightness RGB
img_rgbbright = np.zeros(img.shape, dtype = np.uint8)

#Fungsi untuk menghitung brightness RGB dengan nilai parameter 
def rgbbrighter(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            red += nilai
            if red > 255:
                red = 25
            if red < 0:
                red = 0
            green = img[y][x][1]
            green += nilai
            if green > 255:
                green = 255
            if green < 0:
                green = 0
            blue = img[y][x][2]
            blue += nilai
            if blue > 255:
                blue = 255
            if blue < 0:
                blue = 0
            img_rgbbright[y][x] = (red, green, blue)

rgbbrighter(-100)
cv.imshow('Brightness -100',img_brightness)#Memunculkan gambar dari variabel img_brightness dan memberi judul
cv.waitKey(0)#Tampilan akan menutup dengan bebas menekan tombol tanpa batas waktu
cv.destroyAllWindows()#digunakan untuk menutup seluruh jendela

rgbbrighter(25)
cv.imshow('Brightness +25',img_brightness)#Memunculkan gambar dari variabel img_brightness dan memberi judul
cv.waitKey(0)#Tampilan akan menutup dengan bebas menekan tombol tanpa batas wakt
cv.destroyAllWindows()

#Contrast
img_contrass = np.zeros(img.shape, dtype = np.uint8)
#Menghitung fungsi contrass
def contrass(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]##Mendapatkan itensitas warna merah
            green = img[y][x][1]##Mendapatkan itensitas warna hijau
            blue = img[y][x][2]##Mendapatkan itensitas warna biru
            gray = (int(red) + int(green) + int(blue))/3#rumus fungsi untuk menghasilkan warna abu-abu
            gray += nilai
            if gray > 255:
                gray = 255
            img_contrass[y][x] = (gray, gray, gray)

#Menampilkan gambar dengan parameter 2
contrass(2)
cv.imshow('Contrass 2',img_contrass)#Memunculkan gambar dari variabel img_contrass
cv.waitKey(0)#Tampilan akan menutup dengan bebas menekan tombol tanpa batas waktu
cv.destroyAllWindows()

#Menampilkan gambar dengan parameter 10
contrass(10)
cv.imshow('Contrass 10',img_contrass)
cv.waitKey(0)#Tampilan akan menutup dengan bebas menekan tombol tanpa batas waktu
cv.destroyAllWindows()

img_rgbcontrass = np.zeros(img.shape, dtype = np.uint8)
#Fungsi untuk contrass RGB dengan nilai parameter 
def rgbcontrass(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            red += nilai
            if red > 255:
                red = 255
            green = img[y][x][1]
            green += nilai
            if green > 255:
                green = 255
            blue = img[y][x][2]
            blue += nilai
            if blue > 255:
                blue = 255
            img_rgbcontrass[y][x] = (red, green, blue)

rgbcontrass(2)
cv.imshow('Contrass rgb 2',img_rgbcontrass)
cv.waitKey(0)#Tampilan akan menutup dengan bebas menekan tombol tanpa batas waktu
cv.destroyAllWindows()

rgbcontrass(10)
cv.imshow('Contrass rgb 10',img_rgbcontrass)
cv.waitKey(0)#Tampilan akan menutup dengan bebas menekan tombol tanpa batas waktu
cv.destroyAllWindows()

#Contrast autolevel
img_autocontrass = np.zeros(img.shape, dtype = np.uint8)

def autocontrass():
    xmax = 255
    xmin = 0
    d = 0

    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue))/3
            if gray < xmax:
                xmax = gray
            if gray > xmin:
                xmin = gray
                

    d = xmin - xmax
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue))/3
            gray = int(float(255/d) * (gray - xmax))
            img_autocontrass[y][x] = (gray, gray, gray)

autocontrass()
cv.imshow('Auto level contrass',img_autocontrass)
cv.waitKey(0)#Tampilan akan menutup dengan bebas menekan tombol tanpa batas waktu
cv.destroyAllWindows()

#OPERASI DASAR CITRA

import numpy as np #Mengimport library numpy kemudian di inisialisasi dengan np
import matplotlib.pyplot as plt #Mengimport pyplot dari matplotlib kemudian di inisialisasi dengan plt
from skimage import data#mengimport data dari skimage
from skimage.io import imread#Mengimport membaca dari skimage
from skimage.color import rgb2gray#Mengimport rgb2gray dari skimage
from skimage.util import invert

astronautImage = data.astronaut()#Membuat variabel astronaut image dengan berisi data.astronaut dari skimage
cameraImage = data.camera()#Membuat variabel camera image dengan berisi data.astronaut dari skimage

astroCropped = astronautImage.copy()#Membuat variabel astrocopped dengan besis data dari variabel astronaut Image
astroCropped = astroCropped[0:256,64:320]#Citra di crop diambil dari bagian atas sebesar 256 piksel dan bagian kiri sebesar 64 piksel dari astro crope

cameraCropped = cameraImage.copy()#Membuat variabel astrocopped dengan besis data dari variabel astronaut Image
cameraCropped = cameraCropped[64:256,128:320] #Citra di crop diambil dari bagian tengah sebesar 192 piksel x 192 piksel dari cameraImage.

print('Astro Ori Shape : ',astronautImage.shape)
print('Astro Crop Shape : ',astroCropped.shape)

print('Camera Ori Shape : ',cameraImage.shape)
print('Camera Crop Shape : ',cameraCropped.shape)

fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()

ax[0].imshow(astronautImage)
ax[0].set_title("Citra Input 1")

ax[1].imshow(cameraImage, cmap='gray')
ax[1].set_title('Citra Input 2')

ax[2].imshow(astroCropped)
ax[2].set_title("Citra Output 1")

ax[3].imshow(cameraCropped, cmap='gray')
ax[3].set_title('Citra Output 2')

inv = invert(astroCropped)
print('Shape Input : ', astroCropped.shape)
print('Shape Output : ',inv.shape)

fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()

ax[0].imshow(astroCropped)
ax[0].set_title("Citra Input")

ax[1].hist(astroCropped.ravel(), bins=256)
ax[1].set_title('Histogram Input')

ax[2].imshow(inv)
ax[2].set_title('Citra Output (Inverted Image)')

ax[3].hist(inv.ravel(), bins=256)
ax[3].set_title('Histogram Output')
plt.show()
copyCamera = cameraCropped.copy().astype(float)

m1,n1 = copyCamera.shape
output1 = np.empty([m1, n1])

for baris in range(0, m1-1):
    for kolom in range(0, n1-1):
        a1 = baris
        b1 = kolom
        output1[a1, b1] = copyCamera[baris, kolom] + 100
        
fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()

ax[0].imshow(cameraCropped, cmap='gray')
ax[0].set_title("Citra Input")

ax[1].hist(astroCropped.ravel(), bins=256)
ax[1].set_title('Histogram Input')

ax[2].imshow(output1, cmap='gray')
ax[2].set_title('Citra Output (Brightnes)')

ax[3].hist(output1.ravel(), bins=256)
ax[3].set_title('Histogram Input')
plt.show()

#BRIGHTNESS, CONTRASS, AUTOCONTRASS
#Import dependency
import numpy as np #Mengimport library numpy kemudian di inisialisasi dengan np
import imageio.v3 as imageio # Mengimport library dari imageio
import cv2 as cv #Memasukan atau mengimport library dari cv2
import matplotlib.pyplot as plt #Mengimport pyplot dari matplotlib kemudian di inisialisasi dengan plt

img = plt.imread(r'C:\Users\ASUS\Documents\FILE SYAHDAN\semester 6\PCD\PRAKTIKUM 5\Saitama.JPG')#Membaca gambar format JPEG dengan kode plt dan disimpan dalam variabel img


#Mendapatkan/define resolusi dan tipe gambar
img_height = img.shape[0]#Tinggi gambar disimpan pada variabel img.shape 0
img_width = img.shape[1]#Panjang gambar disimpan pada variabel img.shape 1
img_channel = img.shape[2]# Warna Channel gambar disimpan pada variabel img.shape 2
img_type = img.dtype
#Membuat variabel img_brightness untuk menampung hasil
img_brightness = np.zeros(img.shape, dtype=np.uint8)

#Melakukan penambahan brightness dengan nilai yg menjadi parameter
def brighter(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray += nilai
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_brightness[y][x] = (gray, gray, gray)
            
#Menampilkan beberapa hasil dengan nilai brightness -100 dan 100
brighter(-100)
plt.imshow(img_brightness)
plt.title("Brightness -100")
plt.show()

brighter(100)
plt.imshow(img_brightness)
plt.title("Brightness 100")
plt.show()  

#Membuat variabel img_rgbbrightness untuk menampung hasil
img_rgbbrightness = np.zeros(img.shape, dtype=np.uint8)    

#Melakukan penambahan brightness dengan nilai yg menjadi parameter
def rgbbrighter(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            red += nilai
            if red > 255:
                red = 255
            if red < 0:
                red = 0
            green = img[y][x][1]
            green += nilai
            if green > 255:
                green = 255
            if green < 0:
                green = 0
            blue = img[y][x][2]
            blue += nilai
            if blue > 255:
                blue = 255
            if blue < 0:
                blue = 0
            img_rgbbrightness[y][x] = (red, green, blue) 
            
#Menampilkan beberapa hasil dengan nilai brightness -100 dan 100
rgbbrighter(-100)
plt.imshow(img_rgbbrightness)
plt.title("Brightness -100")
plt.show()

rgbbrighter(100)
plt.imshow(img_rgbbrightness)
plt.title("Brightness 100")
plt.show()

#1. Membuat variabel img_contrass untuk menampung hasil
img_contrass = np.zeros(img.shape, dtype=np.uint8)

#2. Melakukan penambahan contrass dengan nilai yg menjadi parameter
def contrass(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray *= nilai
            if gray > 255:
                gray = 255
            img_contrass[y][x] = (gray, gray, gray)
            
#Menampilkan beberapa hasil dengan nilai contrass 50 dan 100
contrass(2)
plt.imshow(img_contrass)
plt.title("Contrass 2")
plt.show()

contrass(3)
plt.imshow(img_contrass)
plt.title("Contrass 3")
plt.show()      


#1. Membuat variabel img_contrass untuk menampung hasil
img_autocontrass = np.zeros(img.shape, dtype=np.uint8)    


#2. Melakukan penambahan contrass secara otomatis
def autocontrass():
    xmax = 300
    xmin = 0
    d = 0
    # Mendapatkan nilai d, dimana nilai d ini akan berpengaruh pada hitungan
    # untuk mendapatkan tingkat kontras
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            if gray < xmax:
                xmax = gray
            if gray > xmin:
                xmin = gray
    d = xmin-xmax
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(float(255/d) * (gray-xmax))
            img_autocontrass[y][x] = (gray, gray, gray) 
                 
#3. Menampilkan hasil autolevel contrass
autocontrass()
plt.imshow(img_autocontrass)
plt.title("Contrass Autolevel")
plt.show()                 