import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pickup_map.settings.local')
import django
django.setup()

from main.models import Professor


if __name__ == '__main__':
    Professor(id=1, name='아지즈', subject="Data Analytics", email='aziz@chungbuk.ac.kr', site='http://dalab.cbnu.ac.kr', background="""	Work Experience:
2018.03 – Present: Associate Professor, Chungbuk National University, South Korea
2015.09 – 2018.02: Assistant Professor, Chungbuk National University, South Korea
2014.03 – 2015.08: Assistant Professor, Dongguk University at Gyeongju, South Korea
2012.08 – 2014.02: Principle Researcher (Post-Doctoral Researcher), Sookymung Women's University, South Korea

Professional Activities:
Organizing Committee: IEEE Big Data 2020, BIGDAS 2020, BIGDAS 2019, IDEAS 2020, CBDCom 2020, SmartData2019
Program Committee: IEEE Big Data 2020, ACM SAC 2020, IEEE GLOBECOM 2020, Web3D 2020, ACM SAC 2019
Editorial Board Member: JIPS, JMIS
Reviewer: Journal of Machine Learning and Cybernetics, IEEE Transactions on Industrial Informatics, IEEE Access, International Journal of Web and Grid Services, Journal of Supercomputing, WWW Journal, Multimedia Tools and Applications, Applied Science, Electronics, etc.
Member: IEEE, AAAI, KIISE, KIPS, KMMS""", performance="""- U-Ju Gim, Jeong-Hun Kim, Kwan-Hee Yoo, Aziz Nasridinov*, "Motion-Attentive Network for Detecting Abnormal Situations in Surveillance Video," In Proceedings of the ACM SIGGRAPH2020 (h5 index: 20), ACCEPTED.
- Jong-Hyeok Choi, Fei Hao, Aziz Nasridinov*, "HI-Sky: Hash Index-Based Skyline Query Processing," Applied Science (SCIE, IF: 2.474), Vol. 10, No 5, March 2020.
-U-Ju Gim, Jae-Jun Lee, Jeong-Hun Kim, Young-Ho Park, Aziz Nasridinov*, "An Automatic Shoplifting Detection from Surveillance Videos," In Proceedings of the AAAI Conference on Artificial Intelligence (AAAI2020) (h5 index: 126), pp. 13795-13796, New York, USA, February 2020.
- Ga-Ae Ryu, Aziz Nasridinov, HyungChul Rah, Kwan-Hee Yoo, "Forecasts of the Amount Purchase Pork Meat by Using Structured and Unstructured Big Data," Agriculture (SCIE, IF: 2.04), Vol. 10, No 1, January 2020.
- Jeong-Hun Kim, Jong-Hyeok Choi, Kwan-Hee Yoo, Woong-Kee Loh, Aziz Nasridinov*, "A Fast Algorithm for Identifying Density-Based Clustering Structures Using a Constraint Graph," Electronics (SCIE, IF: 2.412), Vol. 8, No. 10, September 2019.
- Sein Jang, Young-Ho Park, Aziz Nasridinov*, "AVS-Net: Automatic Visual Surveillance Using Relation Network," In Proceedings of the AAAI Conference on Artificial Intelligence (AAAI2019) (h5 index: 126), pp. 9947-9948, Hawaii, USA, January 2019.
Jeong-Hun Kim, Jong-Hyeok Choi, Kwan-Hee Yoo, Aziz Nasridinov*, "AA-DBSCAN: an approximate adaptive DBSCAN for finding clusters with varying densities," Journal of Supercomputing (SCI, IF: 2.469), Vol. 75, No 1, pp. 142-169, January 2019.
- Sang Hun Han, Aziz Nasridinov, Keun Ho Ryu, "Information Flow Monitoring System," IEEE Access (SCIE, IF: 4.098), Vol. 6, pp. 23820-23827, 2018.""").save()
    Professor(id=2, name='전중남', subject="Embedded system", email='joongnam@cbnu.ac.kr', site='http://dalab.cbnu.ac.kr', background="Yonsei University", performance="").save()
    Professor(id=3, name='홍장의', subject="소프트웨어공학", email='jehong@chungbuk.ac.kr', site='-', background="KAIST",   performance="").save()