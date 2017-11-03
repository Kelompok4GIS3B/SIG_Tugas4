import folium

def Marker(long,lat):
	m = folium.Map(
    location=[long,lat],
    zoom_start=12,
    tiles='Stamen Terrain')
	return m

def RegularPolygon(long,lat):
	a = folium.Map(
    location=[long,lat],
    zoom_start=12,
    tiles='Stamen Toner')	
	return a
	
def Circle(long,lat):
	n = folium.Map(
    location=[long,lat],
    zoom_start=12,
    tiles='Stamen Toner')	
	return n
	
def disimpan(empat,lima):
	empat.save(lima)
	
n = Circle(-6.202367, 106.655953)
a = RegularPolygon(-6.202367, 106.655953)
m = Marker(-6.202367, 106.655953)
tooltip = 'Click me!'

folium.Marker([-6.200458, 106.660009], popup='<i>Ternak Lele Pak Napis</i>').add_to(m)
folium.Marker([-6.193333, 106.673537], popup='<i>KFC Cipondoh</i>').add_to(m)
folium.Marker([-6.188544, 106.664965], popup='<i>McDonald’s Cipondoh</i>').add_to(m)
folium.Marker([-6.181113, 106.661245], popup='<i>Kings Furniture Tangerang</i>').add_to(m)
folium.Marker([-6.187876, 106.678325], popup='<i>Kongkow Village Cafe</i>').add_to(m)
folium.Marker([-6.188004, 106.658262], popup='<i>Kolam Renang Banjar Wijaya</i>').add_to(m)
folium.Marker([-6.175353, 106.663755], popup='<i>Pasar Royal</i>').add_to(m)
folium.Marker([-6.171430, 106.646498], popup='<i>Stasiun Geofisika Tangerang</i>').add_to(m)
folium.Marker([-6.171526, 106.649170], popup='<i>Nasi Goreng Mas Jangkung</i>').add_to(m)
folium.Marker([-6.170075, 106.646874], popup='<i>Kantor Kelurahan Tanah Tinggi</i>').add_to(m)
folium.Marker([-6.169307, 106.644975], popup='<i> Masjid Al Hakim</i>').add_to(m)
folium.Marker([-6.167344, 106.646842], popup='<i>Komp.LP Wanita tanah tinggi</i>').add_to(m)
folium.Marker([-6.167984, 106.648193], popup='<i>Masjid AL Islah</i>').add_to(m)
folium.Marker([-6.169040, 106.649331], popup='<i>Masjid AL Hikmah</i>').add_to(m)
folium.Marker([-6.168779, 106.647544], popup='<i>DeZie Cafe</i>').add_to(m)
folium.Marker([-6.170065, 106.649191], popup='<i>Warung Sate Solo</i>').add_to(m)
folium.Marker([-6.170342, 106.647501], popup='<i>Lembaga Kebijakan Publik</i>').add_to(m)
folium.Marker([-6.170987, 106.643269], popup='<i>Komplek Imigrasi Tangerang</i>').add_to(m)
folium.Marker([-6.172689, 106.640130], popup='<i>Lapangan Sepak Bola Sukun</i>').add_to(m)
folium.Marker([-6.172747, 106.640796], popup='<i>Lapangan Tembak PERBAKIN Tangerang</i>').add_to(m)
folium.Marker([-6.171286, 106.640082], popup='<i>Dinas Pendidikan</i>').add_to(m)
folium.Marker([-6.171286, 106.640082], popup='<i>Dinas Pendidikan</i>').add_to(m)
folium.Marker([-6.191157, 106.664858], popup='<i>Sekolah Menengah Atas Negeri 10 Tangerang</i>').add_to(m)
folium.Marker([-6.188597, 106.666725], popup='<i>Margoland Cipondoh</i>').add_to(m)
folium.Marker([-6.192309, 106.672497], popup='<i>Narita Hotel Tangerang</i>').add_to(m)
folium.Marker([-6.194869, 106.674589], popup='<i>Jagarawa</i>').add_to(m)
folium.Marker([-6.185685, 106.676606], popup='<i>Sipon Susu</i>').add_to(m)
folium.Marker([-6.183147, 106.691208], popup='<i>Daarul Quran</i>').add_to(m)
folium.Marker([-6.202922, 106.688569], popup='<i>GREEN VILLAGE</i>').add_to(m)
folium.Marker([-6.206527, 106.687163], popup='<i>Dojo Cipondoh</i>').add_to(m)
folium.Marker([-6.203828, 106.687904], popup='<i>Global Cell</i>').add_to(m)
folium.Marker([-6.202527, 106.688333], popup='<i>Cipondoh Jaya Motor</i>').add_to(m)
folium.Marker([-6.179947, 106.708454], popup='<i>Green Lake City Ruko Food City</i>').add_to(m)
folium.Marker([-6.187755, 106.599428], popup='<i>Apotek Taman Cibodas</i>').add_to(m)
folium.Marker([-6.183168, 106.592626], popup='<i>RSIA Gebang Medika</i>').add_to(m)
folium.Marker([-6.188576, 106.591156], popup='<i>Pasar Jatiuwung</i>').add_to(m)
folium.Marker([-6.186715, 106.588838], popup='<i>Chizkek Lumer TANGERANG</i>').add_to(m)
folium.Marker([-6.185131, 106.584515], popup='<i>Kroncong Residence</i>').add_to(m)
folium.Marker([-6.181622, 106.586682], popup='<i>Sekolah Dasar Negeri Keroncong Mas Permai</i>').add_to(m)
folium.Marker([-6.182256, 106.584595], popup='<i>Perumahan Taman Kota Permai 6</i>').add_to(m)
folium.Marker([-6.132065, 106.643042], popup='<i>Posko Garuda City Center</i>').add_to(m)
folium.Marker([-6.132907, 106.642490], popup='<i>PT. Garuda Indonesia</i>').add_to(m)


folium.Marker([-6.172928, 106.664536], popup='Poris Plawad').add_to(m)
folium.Marker([-6.162902, 106.667518], popup='BPJS Kesehatan Batu Ceper').add_to(m)
folium.Marker([-6.163083, 106.671510], popup='Jl. Daan Mogot No.289').add_to(m)
folium.Marker([-6.165089, 106.675592], popup='Jl. Daan Mogot').add_to(m)
folium.Marker([-6.154171, 106.652809], popup='Warung Adelya Menjual Berbagai Macam').add_to(m)
folium.Marker([-6.158405, 106.652627], popup='Pondok Bahar').add_to(m)
folium.Marker([-6.157258, 106.652734], popup='Taman Pendidikan Al-Qur'an (TPA/TPQ)').add_to(m)
folium.Marker([-6.156546, 106.655651], popup='Intan Pertiwi Industri').add_to(m)
folium.Marker([-6.156470, 106.656636], popup='ATM Bank Tabungan Negara (Persero)').add_to(m)
folium.Marker([-6.156690, 106.656489], popup='Harapan Motor Toko').add_to(m)


=======
folium.Marker([-6.196558, 106.654992], popup='Mie Ayam Win').add_to(m)
folium.Marker([-6.196476, 106.654991], popup='Banjar Wijaya Tangerang').add_to(m)
folium.Marker([-6.196275, 106.654995], popup='Es Kelapa Muda Mang Cecep').add_to(m)
folium.Marker([-6.198192, 106.653570], popup='Bengkel Motor Bang Dede').add_to(m)
folium.Marker([-6.195056, 106.653460], popup='Mie Ayam Jantan').add_to(m)
folium.Marker([-6.195408, 106.653541], popup='Nirwana 1 Cluster Nirwana Modernland').add_to(m)
folium.Marker([-6.195503, 106.653694], popup='Cluster Nirwana Kota Modern').add_to(m)
folium.Marker([-6.200795, 106.655701], popup='Dufia isi Ulang').add_to(m)
folium.Marker([-6.199384, 106.655056], popup='Water Park Taman Konblock').add_to(m)
folium.Marker([-6.200544, 106.658478], popup='Kantor Kelurahan Cipete').add_to(m)


%punya hanna

folium.Marker([-6.220371, 106.662390], popup='IKEA Alam Sutera').add_to(m)
folium.Marker([-6.241532, 106.628401], popup='Summarecon Mal').add_to(m)
folium.Marker([-6.127871, 106.652777], popup='Bandar Udara Internasional Soekarno-Hatta').add_to(m)
folium.Marker([-6.193067, 106.680930], popup='Danau Cipondoh').add_to(m)
folium.Marker([-6.158891, 106.583855], popup='Amsterdam Water Park').add_to(m)
folium.Marker([-6.158891, 106.583855], popup='Sekolah Tarsisius Vireta').add_to(m)
folium.Marker([-6.158891, 106.583855], popup='Global Mansion').add_to(m)
folium.Marker([-6.169963, 106.595013], popup='SMA 15 Tangerang').add_to(m)
folium.Marker([-6.187072, 106.603596], popup='Giant Ekstra Gatot Subroto').add_to(m)
folium.Marker([-6.187072, 106.603596], popup='Taman Cibodas Raya').add_to(m)
folium.Marker([-6.177019, 106.650449], popup='Warung Makan Mama Laras').add_to(m)
folium.Marker([-6.177606, 106.646157], popup='Butik Pelangi').add_to(m)
folium.Marker([-6.176699, 106.653163], popup='Masjid Jami Al-Hikmah Tangerang').add_to(m)
folium.Marker([-6.175238, 106.646297], popup='Stasiun Tanah Tinggi').add_to(m)
folium.Marker([-6.174875, 106.652831], popup='Pertamina Spbu 34-15129').add_to(m)
folium.Marker([-6.185595, 106.643679], popup='Apotek Berkat').add_to(m)
folium.Marker([-6.188422, 106.642231], popup='Rumah Makan Cak Mun').add_to(m)
folium.Marker([-6.186651, 106.637757], popup='SMK Negeri 4 Tangerang').add_to(m)
folium.Marker([-6.191152, 106.640289], popup='BRI Tbk.PT').add_to(m)
folium.Marker([-6.194096, 106.641823], popup='Perumahan Cluster Pasadena').add_to(m)
folium.Marker([-6.190755, 106.638422], popup='Akar Sabu').add_to(m)
folium.Marker([-6.189870, 106.634554], popup='Graha Malika').add_to(m)
folium.Marker([-6.189704, 106.636271], popup='UNIS Tangerang').add_to(m)
folium.Marker([-6.196628, 106.639260], popup='Warung Kopi Bang Ade').add_to(m)
folium.Marker([-6.196554, 106.641432], popup='Ayam Tulang Lunak Bu Iin').add_to(m)
folium.Marker([-6.204857, 106.638750], popup='Perumahan Cluster Pulau Dewa Modernland').add_to(m)
folium.Marker([-6.204553, 106.641304], popup='Bakmi Ayam Ijo Mayapada').add_to(m)
folium.Marker([-6.177683, 106.625165], popup='RS Waras').add_to(m)
folium.Marker([-6.179688, 106.621367], popup='Hotel Merdeka').add_to(m)
folium.Marker([-6.185360, 106.620166], popup='Pakis Mas Resindence').add_to(m)
folium.Marker([-6.214656, 106.676742], popup='Starbuck Rest AREA KM 14').add_to(m)
folium.Marker([-6.213085, 106.679135], popup='Pecel Lele Depot Cantik Asih').add_to(m)
folium.Marker([-6.221378, 106.679543], popup='Sekolah Dasar Islam Baiturrachman').add_to(m)
folium.Marker([-6.220125, 106.677419], popup='My Shin Cafe').add_to(m)
folium.Marker([-6.220125, 106.677419], popup='Kantor Kelurahan Cipete').add_to(m)
folium.Marker([-6.202619, 106.660007], popup='Gumay Foundation').add_to(m)
folium.Marker([-6.196998, 106.665049], popup='Pandan Aquarium Toko').add_to(m)
folium.Marker([-6.194565, 106.671339], popup='LPK HIKARI GAKKAI').add_to(m)
folium.Marker([-6.200840, 106.650914], popup='SOYES HOME Soya Milk').add_to(m)
folium.Marker([-6.192851, 106.662379], popup='Masjid Quba Taman Royal 2').add_to(m)
folium.RegularPolygonMarker(
    [-6.191979, 106.591591],
    popup='RS Dinda',
    fill_color='#132b5e',
    number_of_sides=3,
    radius=10
    ).add_to(a)
folium.RegularPolygonMarker(
    [-6.195179, 106.585679],
    popup='BPJS Liasion Office Jatake',
    fill_color='#132b5e',
    number_of_sides=3,
    radius=10
    ).add_to(a)	
a

folium.Circle(
    radius=100,
    location=[-6.189003, 106.579832],
    popup='PT. Pancaprima Ekabrother',
    color='crimson',
    fill=False,
).add_to(n)
n


folium.Marker(
    location=[-6.182490, 106.584710],
    popup='Distibutor NASA N-430321',
    icon=folium.Icon(icon='cloud')
).add_to(m)
m

disimpan(a,'4.html')
disimpan(n,'5.html')
disimpan(m,'6.html')