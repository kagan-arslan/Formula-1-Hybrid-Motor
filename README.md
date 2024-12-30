Elektrikli ve Hibrid Spor Aracı Simülasyonu

Bu proje, elektrikli ve hibrid spor aracının performansını simüle eden bir yazılım çözümüdür. Simülasyon, motor sistemi, enerji geri kazanımı, aerodinamik yapı, lastik performansı ve araç simülasyonu unsurlarını bir araya getirir. Python dili ve çeşitli kütüphaneler kullanılarak, aracın hızlanma, frenleme, aerodinamik drag ve downforce gibi özellikleri hesaplanmaktadır.

Özellikler
	•	Hibrid Motor Modeli: İçten yanmalı motor ve elektrikli motor birleştirerek gücü optimize eder.
	•	Enerji Geri Kazanımı: Frenleme sırasında kazanılan enerjiyi bataryaya aktarır.
	•	Aerodinamik Yapı: Araç aerodinamiği simüle edilerek sürükleme kuvveti ve yere yapışma kuvveti hesaplanır.
	•	Lastik Performansı: Lastiklerin tutuş performansı, simülasyona dahil edilmiştir.
	•	Simülasyon Sonuçları: Simülasyon sonuçları grafikler şeklinde görselleştirilir.

Başlangıç

Gereksinimler

Proje, Python 3.6 ve üzeri sürümleri ile çalışır. Aşağıdaki kütüphanelerin yüklü olduğundan emin olun:
	•	numpy
	•	matplotlib
	•	scipy

Yüklemek için terminalde aşağıdaki komutu kullanabilirsiniz:

pip install numpy matplotlib scipy

Kurulum

Projenin tüm dosyalarını GitHub reposundan klonladıktan sonra, simülasyonu çalıştırabilirsiniz.

Kullanım

Simülasyonu çalıştırmadan önce, parametrelerinizi değiştirebilirsiniz. Aşağıda, bazı parametrelerin nasıl ayarlanacağına dair örnekler bulunmaktadır.

Motor Parametreleri:

# Motor sistemi parametreleri:
hybrid_motor = HybridMotor(
    max_torque_ice=500,
    max_torque_electric=250,
    max_power_ice=700,
    max_power_electric=350,
    rpm_range_ice=[1000, 8000],
    rpm_range_electric=[0, 12000]
)

Enerji Geri Kazanımı:

# Enerji geri kazanımı parametreleri:
energy_system = EnergyRecovery(
    efficiency=0.85,
    battery_capacity=100,
    regen_factor=0.8,
    discharge_rate=0.1
)

Aerodinamik Parametreler:

# Aerodinamik sistem parametreleri:
aero_system = Aerodynamics(
    drag_coefficient=0.5,
    downforce_coefficient=2.0,
    vehicle_weight=700
)

Lastik Performansı:

# Lastik sistemi parametreleri:
tire_system = Tires(
    max_grip=1000,
    tire_diameter=0.7
)

Simülasyonu Başlatma:

Simülasyonu başlatmak için aşağıdaki komutu çalıştırabilirsiniz:

# Simülasyon başlatma
sim = F1Simulation(hybrid_motor, energy_system, aero_system, tire_system)
sim.run_simulation()
sim.plot_results()  # Simülasyon sonuçlarını görselleştirme

Parametre Değiştirme
	•	Hibrid motor parametrelerini içten yanmalı motor (ICE) ve elektrikli motor (EM) güç sınırlamaları, tork ve RPM aralıklarını değiştirebilirsiniz.
	•	Enerji geri kazanımı, enerji verimliliği, batarya kapasitesi ve şarj/boşaltma oranları gibi özellikler, simülasyona dahil edilmiştir.
	•	Aerodinamik parametreler, sürükleme katsayısı (drag_coefficient) ve downforce katsayısını içermektedir.
	•	Lastik parametreleri, lastiklerin maksimum tutuş gücünü (max_grip) ve çapını içerir.

Her parametreyi değiştirerek simülasyonunuzu özelleştirebilirsiniz.

Katkıda Bulunma

Katkıda bulunmak istiyorsanız, lütfen aşağıdaki adımları takip edin:
	1.	Depoyu çatallayın (fork).
	2.	Yeni bir dal (branch) oluşturun.
	3.	Yapmak istediğiniz değişiklikleri yapın.
	4.	Değişikliklerinizi commitleyin.
	5.	Yeni dalı gönderin ve pull request oluşturun.

Lisans

Bu proje, MIT Lisansı altında lisanslanmıştır.

İletişim

Eğer herhangi bir sorunuz ya da öneriniz varsa, lütfen benimle iletişime geçin:
	•	GitHub: github.com/kagan-arslan
	•	E-posta: kaganyusufarslan01@gmail.com
