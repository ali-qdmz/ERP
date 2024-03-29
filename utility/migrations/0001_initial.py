# Generated by Django 3.2.5 on 2021-09-04 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0013_auto_20210718_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='نام ')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات ')),
            ],
            options={
                'verbose_name': 'نوع کسب و کار ',
                'verbose_name_plural': 'نوع کسب و کار',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='نام ')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات ')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='ایمیل ')),
                ('cell_phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='شماره تلفن همراه ')),
                ('land_phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='شماره تلن ثابت ')),
                ('country', models.CharField(blank=True, choices=[('NLD', 'Netherlands'), ('DEU', 'Germany'), ('FRA', 'France'), ('BRA', 'Brazil'), ('USA', 'United States'), ('ABW', 'Aruba'), ('AFG', 'Afghanistan'), ('AGO', 'Angola'), ('AIA', 'Anguilla'), ('ALA', 'Aland Islands'), ('ALB', 'Albania'), ('AND', 'Andorra'), ('ANT', 'Netherlands Antilles'), ('ARE', 'United Arab Emirates'), ('ARG', 'Argentina'), ('ARM', 'Armenia'), ('ASM', 'American Samoa'), ('ATA', 'Antarctica'), ('ATF', 'French Southern Territories'), ('ATG', 'Antigua and Barbuda'), ('AUS', 'Australia'), ('AUT', 'Austria'), ('AZE', 'Azerbaijan'), ('BDI', 'Burundi'), ('BEL', 'Belgium'), ('BEN', 'Benin'), ('BFA', 'Burkina Faso'), ('BGD', 'Bangladesh'), ('BGR', 'Bulgaria'), ('BHR', 'Bahrain'), ('BHS', 'Bahamas'), ('BIH', 'Bosnia and Herzegovina'), ('BLM', 'Saint Barthelemy'), ('BLR', 'Belarus'), ('BLZ', 'Belize'), ('BMU', 'Bermuda'), ('BOL', 'Bolivia, Plurinational State of'), ('BRB', 'Barbados'), ('BRN', 'Brunei Darussalam'), ('BTN', 'Bhutan'), ('BVT', 'Bouvet Island'), ('BWA', 'Botswana'), ('CAF', 'Central African Republic'), ('CAN', 'Canada'), ('CCK', 'Cocos (Keeling) Islands'), ('CHE', 'Switzerland'), ('CHL', 'Chile'), ('CHN', 'China'), ('CIV', "Cote d'Ivoire"), ('CMR', 'Cameroon'), ('COD', 'Congo, the Democratic Republic of the'), ('COG', 'Congo'), ('COK', 'Cook Islands'), ('COL', 'Colombia'), ('COM', 'Comoros'), ('CPV', 'Cape Verde'), ('CRI', 'Costa Rica'), ('CUB', 'Cuba'), ('CXR', 'Christmas Island'), ('CYM', 'Cayman Islands'), ('CYP', 'Cyprus'), ('CZE', 'Czech Republic'), ('DJI', 'Djibouti'), ('DMA', 'Dominica'), ('DNK', 'Denmark'), ('DOM', 'Dominican Republic'), ('DZA', 'Algeria'), ('ECU', 'Ecuador'), ('EGY', 'Egypt'), ('ERI', 'Eritrea'), ('ESH', 'Western Sahara'), ('ESP', 'Spain'), ('EST', 'Estonia'), ('ETH', 'Ethiopia'), ('FIN', 'Finland'), ('FJI', 'Fiji'), ('FLK', 'Falkland Islands (Malvinas)'), ('FRO', 'Faroe Islands'), ('FSM', 'Micronesia, Federated States of'), ('GAB', 'Gabon'), ('GBR', 'United Kingdom'), ('GEO', 'Georgia'), ('GGY', 'Guernsey'), ('GHA', 'Ghana'), ('GIB', 'Gibraltar'), ('GIN', 'Guinea'), ('GLP', 'Guadeloupe'), ('GMB', 'Gambia'), ('GNB', 'Guinea-Bissau'), ('GNQ', 'Equatorial Guinea'), ('GRC', 'Greece'), ('GRD', 'Grenada'), ('GRL', 'Greenland'), ('GTM', 'Guatemala'), ('GUF', 'French Guiana'), ('GUM', 'Guam'), ('GUY', 'Guyana'), ('HKG', 'Hong Kong'), ('HMD', 'Heard Island and McDonald Islands'), ('HND', 'Honduras'), ('HRV', 'Croatia'), ('HTI', 'Haiti'), ('HUN', 'Hungary'), ('IDN', 'Indonesia'), ('IMN', 'Isle of Man'), ('IND', 'India'), ('IOT', 'British Indian Ocean Territory'), ('IRL', 'Ireland'), ('IRN', 'Iran, Islamic Republic of'), ('IRQ', 'Iraq'), ('ISL', 'Iceland'), ('ISR', 'Israel'), ('ITA', 'Italy'), ('JAM', 'Jamaica'), ('JEY', 'Jersey'), ('JOR', 'Jordan'), ('JPN', 'Japan'), ('KAZ', 'Kazakhstan'), ('KEN', 'Kenya'), ('KGZ', 'Kyrgyzstan'), ('KHM', 'Cambodia'), ('KIR', 'Kiribati'), ('KNA', 'Saint Kitts and Nevis'), ('KOR', 'Korea, Republic of'), ('KWT', 'Kuwait'), ('LAO', "Lao People's Democratic Republic"), ('LBN', 'Lebanon'), ('LBR', 'Liberia'), ('LBY', 'Libyan Arab Jamahiriya'), ('LCA', 'Saint Lucia'), ('LIE', 'Liechtenstein'), ('LKA', 'Sri Lanka'), ('LSO', 'Lesotho'), ('LTU', 'Lithuania'), ('LUX', 'Luxembourg'), ('LVA', 'Latvia'), ('MAC', 'Macao'), ('MAF', 'Saint Martin (French part)'), ('MAR', 'Morocco'), ('MCO', 'Monaco'), ('MDA', 'Moldova, Republic of'), ('MDG', 'Madagascar'), ('MDV', 'Maldives'), ('MEX', 'Mexico'), ('MHL', 'Marshall Islands'), ('MKD', 'Macedonia, the former Yugoslav Republic of'), ('MLI', 'Mali'), ('MLT', 'Malta'), ('MMR', 'Myanmar'), ('MNE', 'Montenegro'), ('MNG', 'Mongolia'), ('MNP', 'Northern Mariana Islands'), ('MOZ', 'Mozambique'), ('MRT', 'Mauritania'), ('MSR', 'Montserrat'), ('MTQ', 'Martinique'), ('MUS', 'Mauritius'), ('MWI', 'Malawi'), ('MYS', 'Malaysia'), ('MYT', 'Mayotte'), ('NAM', 'Namibia'), ('NCL', 'New Caledonia'), ('NER', 'Niger'), ('NFK', 'Norfolk Island'), ('NGA', 'Nigeria'), ('NIC', 'Nicaragua'), ('NIU', 'Niue'), ('NOR', 'Norway'), ('NPL', 'Nepal'), ('NRU', 'Nauru'), ('NZL', 'New Zealand'), ('OMN', 'Oman'), ('PAK', 'Pakistan'), ('PAN', 'Panama'), ('PCN', 'Pitcairn'), ('PER', 'Peru'), ('PHL', 'Philippines'), ('PLW', 'Palau'), ('PNG', 'Papua New Guinea'), ('POL', 'Poland'), ('PRI', 'Puerto Rico'), ('PRK', 'North Korea'), ('PRT', 'Portugal'), ('PRY', 'Paraguay'), ('PSE', 'Palestinian Territory, Occupied'), ('PYF', 'French Polynesia'), ('QAT', 'Qatar'), ('REU', 'Reunion'), ('ROU', 'Romania'), ('RUS', 'Russian Federation'), ('RWA', 'Rwanda'), ('SAU', 'Saudi Arabia'), ('SDN', 'Sudan'), ('SEN', 'Senegal'), ('SGP', 'Singapore'), ('SGS', 'South Georgia and the South Sandwich Islands'), ('SHN', 'Saint Helena, Ascension and Tristan da Cunha'), ('SJM', 'Svalbard and Jan Mayen'), ('SLB', 'Solomon Islands'), ('SLE', 'Sierra Leone'), ('SLV', 'El Salvador'), ('SMR', 'San Marino'), ('SOM', 'Somalia'), ('SPM', 'Saint Pierre and Miquelon'), ('SRB', 'Serbia'), ('STP', 'Sao Tome and Principe'), ('SUR', 'Suriname'), ('SVK', 'Slovakia'), ('SVN', 'Slovenia'), ('SWE', 'Sweden'), ('SWZ', 'Swaziland'), ('SYC', 'Seychelles'), ('SYR', 'Syrian Arab Republic'), ('TCA', 'Turks and Caicos Islands'), ('TCD', 'Chad'), ('TGO', 'Togo'), ('THA', 'Thailand'), ('TJK', 'Tajikistan'), ('TKL', 'Tokelau'), ('TKM', 'Turkmenistan'), ('TLS', 'Timor-Leste'), ('TON', 'Tonga'), ('TTO', 'Trinidad and Tobago'), ('TUN', 'Tunisia'), ('TUR', 'Turkey'), ('TUV', 'Tuvalu'), ('TWN', 'Taiwan, Province of China'), ('TZA', 'Tanzania, United Republic of'), ('UGA', 'Uganda'), ('UKR', 'Ukraine'), ('UMI', 'United States Minor Outlying Islands'), ('URY', 'Uruguay'), ('UZB', 'Uzbekistan'), ('VAT', 'Holy See (Vatican City State)'), ('VCT', 'Saint Vincent and the Grenadines'), ('VEN', 'Venezuela, Bolivarian Republic of'), ('VGB', 'Virgin Islands, British'), ('VIR', 'Virgin Islands, U.S.'), ('VNM', 'Viet Nam'), ('VUT', 'Vanuatu'), ('WLF', 'Wallis and Futuna'), ('WSM', 'Samoa'), ('YEM', 'Yemen'), ('ZAF', 'South Africa'), ('ZMB', 'Zambia'), ('ZWE', 'Zimbabwe')], max_length=32, verbose_name='کشور ')),
                ('state', models.CharField(blank=True, max_length=255, null=True, verbose_name='استان ')),
                ('city', models.CharField(blank=True, max_length=255, null=True, verbose_name='شهر ')),
                ('zip_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='کدپستی ')),
                ('about', models.TextField(blank=True, null=True, verbose_name='درباره ')),
                ('contact_details', models.TextField(blank=True, null=True, verbose_name='اطلاعات تماس ')),
                ('latitude', models.CharField(blank=True, max_length=512, null=True, verbose_name='عرض جغرافیایی ')),
                ('longitude', models.CharField(blank=True, max_length=512, null=True, verbose_name='طول جغرافیایی ')),
                ('year_established', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='سال تاسیس ')),
                ('total_employees', models.CharField(blank=True, max_length=255, null=True, verbose_name='تعداد کارمندان ')),
                ('business_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='نوع کسب و کار ')),
                ('main_products', models.CharField(blank=True, max_length=255, null=True, verbose_name='تولیدات اصلی ')),
                ('total_annual_revenue', models.CharField(blank=True, max_length=255, null=True, verbose_name='مجموع عایدی سالانه ')),
                ('url', models.CharField(blank=True, max_length=255, null=True, verbose_name='لینک ')),
                ('social_link', models.CharField(blank=True, max_length=255, null=True, verbose_name='شبکه ی اجتماعی ')),
            ],
            options={
                'verbose_name': 'کمپانی',
                'verbose_name_plural': 'کمپانی ها',
            },
        ),
        migrations.CreateModel(
            name='ScheduleBaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=255, null=True, verbose_name='موضوع ')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات ')),
                ('date_from', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='از تاریخ ')),
                ('time_from', models.TimeField(blank=True, null=True, verbose_name='از زمان ')),
                ('date_to', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='تا تاریخ ')),
                ('time_to', models.TimeField(blank=True, null=True, verbose_name='تا زمان ')),
            ],
            options={
                'verbose_name': 'مدل اصلی برنامه ریزی',
                'verbose_name_plural': 'مدل های اصلی برنامه ریزی',
            },
        ),
        migrations.CreateModel(
            name='TaskUnitsPointsBaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_units_task', models.DecimalField(decimal_places=2, default='0.00', max_digits=12, verbose_name='مجموع عملیات های واحد ')),
                ('unit_task_description', models.TextField(blank=True, null=True, verbose_name='توضیح عملیات واحد ')),
                ('points_on_unit_task', models.DecimalField(decimal_places=2, default='0.00', max_digits=12, verbose_name='امتیاز عملیات واحد ')),
            ],
            options={
                'verbose_name': 'امتیاز واحد عملیات',
                'verbose_name_plural': 'امتیازات واحد عملیات',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='نام ')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات ')),
            ],
            options={
                'verbose_name': 'واحد',
                'verbose_name_plural': 'واحد ها',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to='auth.user', verbose_name='کاربر ')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='نام ')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='نام خانوادگی ')),
                ('gender', models.CharField(blank=True, choices=[('مرد', 'مرد'), ('زن', 'زن'), ('دیگر', 'دیگر')], max_length=32, verbose_name='جنسیت ')),
                ('date_of_birth', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='تاریخ تولد ')),
                ('nationalid', models.CharField(blank=True, max_length=255, null=True, verbose_name='کد ملی ')),
                ('blood_group', models.CharField(blank=True, max_length=255, null=True, verbose_name='گروه خونی ')),
                ('marital_status', models.CharField(blank=True, max_length=255, null=True, verbose_name='وضعیت نظام وظیفه ')),
                ('name_spouse', models.CharField(blank=True, max_length=255, null=True, verbose_name='نام همسر ')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='ایمیل ')),
                ('cell_phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='شماره تلفن همراه ')),
                ('land_phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='شماره تلفن ثابت ')),
                ('country', models.CharField(blank=True, choices=[('NLD', 'Netherlands'), ('DEU', 'Germany'), ('FRA', 'France'), ('BRA', 'Brazil'), ('USA', 'United States'), ('ABW', 'Aruba'), ('AFG', 'Afghanistan'), ('AGO', 'Angola'), ('AIA', 'Anguilla'), ('ALA', 'Aland Islands'), ('ALB', 'Albania'), ('AND', 'Andorra'), ('ANT', 'Netherlands Antilles'), ('ARE', 'United Arab Emirates'), ('ARG', 'Argentina'), ('ARM', 'Armenia'), ('ASM', 'American Samoa'), ('ATA', 'Antarctica'), ('ATF', 'French Southern Territories'), ('ATG', 'Antigua and Barbuda'), ('AUS', 'Australia'), ('AUT', 'Austria'), ('AZE', 'Azerbaijan'), ('BDI', 'Burundi'), ('BEL', 'Belgium'), ('BEN', 'Benin'), ('BFA', 'Burkina Faso'), ('BGD', 'Bangladesh'), ('BGR', 'Bulgaria'), ('BHR', 'Bahrain'), ('BHS', 'Bahamas'), ('BIH', 'Bosnia and Herzegovina'), ('BLM', 'Saint Barthelemy'), ('BLR', 'Belarus'), ('BLZ', 'Belize'), ('BMU', 'Bermuda'), ('BOL', 'Bolivia, Plurinational State of'), ('BRB', 'Barbados'), ('BRN', 'Brunei Darussalam'), ('BTN', 'Bhutan'), ('BVT', 'Bouvet Island'), ('BWA', 'Botswana'), ('CAF', 'Central African Republic'), ('CAN', 'Canada'), ('CCK', 'Cocos (Keeling) Islands'), ('CHE', 'Switzerland'), ('CHL', 'Chile'), ('CHN', 'China'), ('CIV', "Cote d'Ivoire"), ('CMR', 'Cameroon'), ('COD', 'Congo, the Democratic Republic of the'), ('COG', 'Congo'), ('COK', 'Cook Islands'), ('COL', 'Colombia'), ('COM', 'Comoros'), ('CPV', 'Cape Verde'), ('CRI', 'Costa Rica'), ('CUB', 'Cuba'), ('CXR', 'Christmas Island'), ('CYM', 'Cayman Islands'), ('CYP', 'Cyprus'), ('CZE', 'Czech Republic'), ('DJI', 'Djibouti'), ('DMA', 'Dominica'), ('DNK', 'Denmark'), ('DOM', 'Dominican Republic'), ('DZA', 'Algeria'), ('ECU', 'Ecuador'), ('EGY', 'Egypt'), ('ERI', 'Eritrea'), ('ESH', 'Western Sahara'), ('ESP', 'Spain'), ('EST', 'Estonia'), ('ETH', 'Ethiopia'), ('FIN', 'Finland'), ('FJI', 'Fiji'), ('FLK', 'Falkland Islands (Malvinas)'), ('FRO', 'Faroe Islands'), ('FSM', 'Micronesia, Federated States of'), ('GAB', 'Gabon'), ('GBR', 'United Kingdom'), ('GEO', 'Georgia'), ('GGY', 'Guernsey'), ('GHA', 'Ghana'), ('GIB', 'Gibraltar'), ('GIN', 'Guinea'), ('GLP', 'Guadeloupe'), ('GMB', 'Gambia'), ('GNB', 'Guinea-Bissau'), ('GNQ', 'Equatorial Guinea'), ('GRC', 'Greece'), ('GRD', 'Grenada'), ('GRL', 'Greenland'), ('GTM', 'Guatemala'), ('GUF', 'French Guiana'), ('GUM', 'Guam'), ('GUY', 'Guyana'), ('HKG', 'Hong Kong'), ('HMD', 'Heard Island and McDonald Islands'), ('HND', 'Honduras'), ('HRV', 'Croatia'), ('HTI', 'Haiti'), ('HUN', 'Hungary'), ('IDN', 'Indonesia'), ('IMN', 'Isle of Man'), ('IND', 'India'), ('IOT', 'British Indian Ocean Territory'), ('IRL', 'Ireland'), ('IRN', 'Iran, Islamic Republic of'), ('IRQ', 'Iraq'), ('ISL', 'Iceland'), ('ISR', 'Israel'), ('ITA', 'Italy'), ('JAM', 'Jamaica'), ('JEY', 'Jersey'), ('JOR', 'Jordan'), ('JPN', 'Japan'), ('KAZ', 'Kazakhstan'), ('KEN', 'Kenya'), ('KGZ', 'Kyrgyzstan'), ('KHM', 'Cambodia'), ('KIR', 'Kiribati'), ('KNA', 'Saint Kitts and Nevis'), ('KOR', 'Korea, Republic of'), ('KWT', 'Kuwait'), ('LAO', "Lao People's Democratic Republic"), ('LBN', 'Lebanon'), ('LBR', 'Liberia'), ('LBY', 'Libyan Arab Jamahiriya'), ('LCA', 'Saint Lucia'), ('LIE', 'Liechtenstein'), ('LKA', 'Sri Lanka'), ('LSO', 'Lesotho'), ('LTU', 'Lithuania'), ('LUX', 'Luxembourg'), ('LVA', 'Latvia'), ('MAC', 'Macao'), ('MAF', 'Saint Martin (French part)'), ('MAR', 'Morocco'), ('MCO', 'Monaco'), ('MDA', 'Moldova, Republic of'), ('MDG', 'Madagascar'), ('MDV', 'Maldives'), ('MEX', 'Mexico'), ('MHL', 'Marshall Islands'), ('MKD', 'Macedonia, the former Yugoslav Republic of'), ('MLI', 'Mali'), ('MLT', 'Malta'), ('MMR', 'Myanmar'), ('MNE', 'Montenegro'), ('MNG', 'Mongolia'), ('MNP', 'Northern Mariana Islands'), ('MOZ', 'Mozambique'), ('MRT', 'Mauritania'), ('MSR', 'Montserrat'), ('MTQ', 'Martinique'), ('MUS', 'Mauritius'), ('MWI', 'Malawi'), ('MYS', 'Malaysia'), ('MYT', 'Mayotte'), ('NAM', 'Namibia'), ('NCL', 'New Caledonia'), ('NER', 'Niger'), ('NFK', 'Norfolk Island'), ('NGA', 'Nigeria'), ('NIC', 'Nicaragua'), ('NIU', 'Niue'), ('NOR', 'Norway'), ('NPL', 'Nepal'), ('NRU', 'Nauru'), ('NZL', 'New Zealand'), ('OMN', 'Oman'), ('PAK', 'Pakistan'), ('PAN', 'Panama'), ('PCN', 'Pitcairn'), ('PER', 'Peru'), ('PHL', 'Philippines'), ('PLW', 'Palau'), ('PNG', 'Papua New Guinea'), ('POL', 'Poland'), ('PRI', 'Puerto Rico'), ('PRK', 'North Korea'), ('PRT', 'Portugal'), ('PRY', 'Paraguay'), ('PSE', 'Palestinian Territory, Occupied'), ('PYF', 'French Polynesia'), ('QAT', 'Qatar'), ('REU', 'Reunion'), ('ROU', 'Romania'), ('RUS', 'Russian Federation'), ('RWA', 'Rwanda'), ('SAU', 'Saudi Arabia'), ('SDN', 'Sudan'), ('SEN', 'Senegal'), ('SGP', 'Singapore'), ('SGS', 'South Georgia and the South Sandwich Islands'), ('SHN', 'Saint Helena, Ascension and Tristan da Cunha'), ('SJM', 'Svalbard and Jan Mayen'), ('SLB', 'Solomon Islands'), ('SLE', 'Sierra Leone'), ('SLV', 'El Salvador'), ('SMR', 'San Marino'), ('SOM', 'Somalia'), ('SPM', 'Saint Pierre and Miquelon'), ('SRB', 'Serbia'), ('STP', 'Sao Tome and Principe'), ('SUR', 'Suriname'), ('SVK', 'Slovakia'), ('SVN', 'Slovenia'), ('SWE', 'Sweden'), ('SWZ', 'Swaziland'), ('SYC', 'Seychelles'), ('SYR', 'Syrian Arab Republic'), ('TCA', 'Turks and Caicos Islands'), ('TCD', 'Chad'), ('TGO', 'Togo'), ('THA', 'Thailand'), ('TJK', 'Tajikistan'), ('TKL', 'Tokelau'), ('TKM', 'Turkmenistan'), ('TLS', 'Timor-Leste'), ('TON', 'Tonga'), ('TTO', 'Trinidad and Tobago'), ('TUN', 'Tunisia'), ('TUR', 'Turkey'), ('TUV', 'Tuvalu'), ('TWN', 'Taiwan, Province of China'), ('TZA', 'Tanzania, United Republic of'), ('UGA', 'Uganda'), ('UKR', 'Ukraine'), ('UMI', 'United States Minor Outlying Islands'), ('URY', 'Uruguay'), ('UZB', 'Uzbekistan'), ('VAT', 'Holy See (Vatican City State)'), ('VCT', 'Saint Vincent and the Grenadines'), ('VEN', 'Venezuela, Bolivarian Republic of'), ('VGB', 'Virgin Islands, British'), ('VIR', 'Virgin Islands, U.S.'), ('VNM', 'Viet Nam'), ('VUT', 'Vanuatu'), ('WLF', 'Wallis and Futuna'), ('WSM', 'Samoa'), ('YEM', 'Yemen'), ('ZAF', 'South Africa'), ('ZMB', 'Zambia'), ('ZWE', 'Zimbabwe')], max_length=32, verbose_name='کشور ')),
                ('state', models.CharField(blank=True, max_length=255, null=True, verbose_name='استان ')),
                ('city', models.CharField(blank=True, max_length=255, null=True, verbose_name='شهر ')),
                ('zip_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='کدپستی ')),
                ('permanent_address', models.TextField(blank=True, null=True, verbose_name='آدرس دایمی ')),
                ('about', models.TextField(blank=True, null=True, verbose_name='درباره ')),
                ('contact_details', models.TextField(blank=True, null=True, verbose_name='جزییات اطلاعات تماس ')),
                ('latitude', models.CharField(blank=True, max_length=512, null=True, verbose_name='عرض جغرافیایی ')),
                ('longitude', models.CharField(blank=True, max_length=512, null=True, verbose_name='طول جغرافیایی ')),
            ],
            options={
                'verbose_name': 'پروفایل کاربری',
                'verbose_name_plural': 'پروفایل های کاربری',
            },
        ),
        migrations.CreateModel(
            name='Vat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vat', models.FloatField(blank=True, null=True, verbose_name='درصد مالیات بر ارزش افزوده')),
                ('business_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='VatBusinessType', to='utility.businesstype', verbose_name='نوع تجارت ')),
            ],
            options={
                'verbose_name': 'مالیات بر ارزش افزوده',
                'verbose_name_plural': 'مالیات ها بر ارزش افزوده',
            },
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax', models.FloatField(blank=True, null=True, verbose_name='مالیات ')),
                ('business_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TaxBusinessType', to='utility.businesstype', verbose_name='نوع تجارت ')),
            ],
            options={
                'verbose_name': 'مالیات',
                'verbose_name_plural': 'مالیات ها',
            },
        ),
        migrations.CreateModel(
            name='PredfinedPointsRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True, verbose_name='ایجاد شده در تاریخ ')),
                ('modified_on', django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='تغییر داده شده در تاریخ ')),
                ('units_points', models.DecimalField(decimal_places=2, default='0.00', max_digits=12, verbose_name='امتیاز واحد ')),
                ('task_description', models.TextField(blank=True, null=True, verbose_name='توضیحات عملیات ')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='نظرات ')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='predfinedpointsrule_createdby', to=settings.AUTH_USER_MODEL, verbose_name='ایجاد شده توسط ')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='predfinedpointsrule_modifiedby', to=settings.AUTH_USER_MODEL, verbose_name='تغییر داده شده توسط ')),
            ],
            options={
                'verbose_name': 'قوانین امتیاز',
                'verbose_name_plural': 'قوانین امتیازات',
            },
        ),
        migrations.CreateModel(
            name='CompanyBranch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='نام ')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات ')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='ایمیل ')),
                ('cell_phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='شماره تلفن همراه ')),
                ('land_phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='شمره تلفن ثابت ')),
                ('country', models.CharField(blank=True, choices=[('NLD', 'Netherlands'), ('DEU', 'Germany'), ('FRA', 'France'), ('BRA', 'Brazil'), ('USA', 'United States'), ('ABW', 'Aruba'), ('AFG', 'Afghanistan'), ('AGO', 'Angola'), ('AIA', 'Anguilla'), ('ALA', 'Aland Islands'), ('ALB', 'Albania'), ('AND', 'Andorra'), ('ANT', 'Netherlands Antilles'), ('ARE', 'United Arab Emirates'), ('ARG', 'Argentina'), ('ARM', 'Armenia'), ('ASM', 'American Samoa'), ('ATA', 'Antarctica'), ('ATF', 'French Southern Territories'), ('ATG', 'Antigua and Barbuda'), ('AUS', 'Australia'), ('AUT', 'Austria'), ('AZE', 'Azerbaijan'), ('BDI', 'Burundi'), ('BEL', 'Belgium'), ('BEN', 'Benin'), ('BFA', 'Burkina Faso'), ('BGD', 'Bangladesh'), ('BGR', 'Bulgaria'), ('BHR', 'Bahrain'), ('BHS', 'Bahamas'), ('BIH', 'Bosnia and Herzegovina'), ('BLM', 'Saint Barthelemy'), ('BLR', 'Belarus'), ('BLZ', 'Belize'), ('BMU', 'Bermuda'), ('BOL', 'Bolivia, Plurinational State of'), ('BRB', 'Barbados'), ('BRN', 'Brunei Darussalam'), ('BTN', 'Bhutan'), ('BVT', 'Bouvet Island'), ('BWA', 'Botswana'), ('CAF', 'Central African Republic'), ('CAN', 'Canada'), ('CCK', 'Cocos (Keeling) Islands'), ('CHE', 'Switzerland'), ('CHL', 'Chile'), ('CHN', 'China'), ('CIV', "Cote d'Ivoire"), ('CMR', 'Cameroon'), ('COD', 'Congo, the Democratic Republic of the'), ('COG', 'Congo'), ('COK', 'Cook Islands'), ('COL', 'Colombia'), ('COM', 'Comoros'), ('CPV', 'Cape Verde'), ('CRI', 'Costa Rica'), ('CUB', 'Cuba'), ('CXR', 'Christmas Island'), ('CYM', 'Cayman Islands'), ('CYP', 'Cyprus'), ('CZE', 'Czech Republic'), ('DJI', 'Djibouti'), ('DMA', 'Dominica'), ('DNK', 'Denmark'), ('DOM', 'Dominican Republic'), ('DZA', 'Algeria'), ('ECU', 'Ecuador'), ('EGY', 'Egypt'), ('ERI', 'Eritrea'), ('ESH', 'Western Sahara'), ('ESP', 'Spain'), ('EST', 'Estonia'), ('ETH', 'Ethiopia'), ('FIN', 'Finland'), ('FJI', 'Fiji'), ('FLK', 'Falkland Islands (Malvinas)'), ('FRO', 'Faroe Islands'), ('FSM', 'Micronesia, Federated States of'), ('GAB', 'Gabon'), ('GBR', 'United Kingdom'), ('GEO', 'Georgia'), ('GGY', 'Guernsey'), ('GHA', 'Ghana'), ('GIB', 'Gibraltar'), ('GIN', 'Guinea'), ('GLP', 'Guadeloupe'), ('GMB', 'Gambia'), ('GNB', 'Guinea-Bissau'), ('GNQ', 'Equatorial Guinea'), ('GRC', 'Greece'), ('GRD', 'Grenada'), ('GRL', 'Greenland'), ('GTM', 'Guatemala'), ('GUF', 'French Guiana'), ('GUM', 'Guam'), ('GUY', 'Guyana'), ('HKG', 'Hong Kong'), ('HMD', 'Heard Island and McDonald Islands'), ('HND', 'Honduras'), ('HRV', 'Croatia'), ('HTI', 'Haiti'), ('HUN', 'Hungary'), ('IDN', 'Indonesia'), ('IMN', 'Isle of Man'), ('IND', 'India'), ('IOT', 'British Indian Ocean Territory'), ('IRL', 'Ireland'), ('IRN', 'Iran, Islamic Republic of'), ('IRQ', 'Iraq'), ('ISL', 'Iceland'), ('ISR', 'Israel'), ('ITA', 'Italy'), ('JAM', 'Jamaica'), ('JEY', 'Jersey'), ('JOR', 'Jordan'), ('JPN', 'Japan'), ('KAZ', 'Kazakhstan'), ('KEN', 'Kenya'), ('KGZ', 'Kyrgyzstan'), ('KHM', 'Cambodia'), ('KIR', 'Kiribati'), ('KNA', 'Saint Kitts and Nevis'), ('KOR', 'Korea, Republic of'), ('KWT', 'Kuwait'), ('LAO', "Lao People's Democratic Republic"), ('LBN', 'Lebanon'), ('LBR', 'Liberia'), ('LBY', 'Libyan Arab Jamahiriya'), ('LCA', 'Saint Lucia'), ('LIE', 'Liechtenstein'), ('LKA', 'Sri Lanka'), ('LSO', 'Lesotho'), ('LTU', 'Lithuania'), ('LUX', 'Luxembourg'), ('LVA', 'Latvia'), ('MAC', 'Macao'), ('MAF', 'Saint Martin (French part)'), ('MAR', 'Morocco'), ('MCO', 'Monaco'), ('MDA', 'Moldova, Republic of'), ('MDG', 'Madagascar'), ('MDV', 'Maldives'), ('MEX', 'Mexico'), ('MHL', 'Marshall Islands'), ('MKD', 'Macedonia, the former Yugoslav Republic of'), ('MLI', 'Mali'), ('MLT', 'Malta'), ('MMR', 'Myanmar'), ('MNE', 'Montenegro'), ('MNG', 'Mongolia'), ('MNP', 'Northern Mariana Islands'), ('MOZ', 'Mozambique'), ('MRT', 'Mauritania'), ('MSR', 'Montserrat'), ('MTQ', 'Martinique'), ('MUS', 'Mauritius'), ('MWI', 'Malawi'), ('MYS', 'Malaysia'), ('MYT', 'Mayotte'), ('NAM', 'Namibia'), ('NCL', 'New Caledonia'), ('NER', 'Niger'), ('NFK', 'Norfolk Island'), ('NGA', 'Nigeria'), ('NIC', 'Nicaragua'), ('NIU', 'Niue'), ('NOR', 'Norway'), ('NPL', 'Nepal'), ('NRU', 'Nauru'), ('NZL', 'New Zealand'), ('OMN', 'Oman'), ('PAK', 'Pakistan'), ('PAN', 'Panama'), ('PCN', 'Pitcairn'), ('PER', 'Peru'), ('PHL', 'Philippines'), ('PLW', 'Palau'), ('PNG', 'Papua New Guinea'), ('POL', 'Poland'), ('PRI', 'Puerto Rico'), ('PRK', 'North Korea'), ('PRT', 'Portugal'), ('PRY', 'Paraguay'), ('PSE', 'Palestinian Territory, Occupied'), ('PYF', 'French Polynesia'), ('QAT', 'Qatar'), ('REU', 'Reunion'), ('ROU', 'Romania'), ('RUS', 'Russian Federation'), ('RWA', 'Rwanda'), ('SAU', 'Saudi Arabia'), ('SDN', 'Sudan'), ('SEN', 'Senegal'), ('SGP', 'Singapore'), ('SGS', 'South Georgia and the South Sandwich Islands'), ('SHN', 'Saint Helena, Ascension and Tristan da Cunha'), ('SJM', 'Svalbard and Jan Mayen'), ('SLB', 'Solomon Islands'), ('SLE', 'Sierra Leone'), ('SLV', 'El Salvador'), ('SMR', 'San Marino'), ('SOM', 'Somalia'), ('SPM', 'Saint Pierre and Miquelon'), ('SRB', 'Serbia'), ('STP', 'Sao Tome and Principe'), ('SUR', 'Suriname'), ('SVK', 'Slovakia'), ('SVN', 'Slovenia'), ('SWE', 'Sweden'), ('SWZ', 'Swaziland'), ('SYC', 'Seychelles'), ('SYR', 'Syrian Arab Republic'), ('TCA', 'Turks and Caicos Islands'), ('TCD', 'Chad'), ('TGO', 'Togo'), ('THA', 'Thailand'), ('TJK', 'Tajikistan'), ('TKL', 'Tokelau'), ('TKM', 'Turkmenistan'), ('TLS', 'Timor-Leste'), ('TON', 'Tonga'), ('TTO', 'Trinidad and Tobago'), ('TUN', 'Tunisia'), ('TUR', 'Turkey'), ('TUV', 'Tuvalu'), ('TWN', 'Taiwan, Province of China'), ('TZA', 'Tanzania, United Republic of'), ('UGA', 'Uganda'), ('UKR', 'Ukraine'), ('UMI', 'United States Minor Outlying Islands'), ('URY', 'Uruguay'), ('UZB', 'Uzbekistan'), ('VAT', 'Holy See (Vatican City State)'), ('VCT', 'Saint Vincent and the Grenadines'), ('VEN', 'Venezuela, Bolivarian Republic of'), ('VGB', 'Virgin Islands, British'), ('VIR', 'Virgin Islands, U.S.'), ('VNM', 'Viet Nam'), ('VUT', 'Vanuatu'), ('WLF', 'Wallis and Futuna'), ('WSM', 'Samoa'), ('YEM', 'Yemen'), ('ZAF', 'South Africa'), ('ZMB', 'Zambia'), ('ZWE', 'Zimbabwe')], max_length=32, verbose_name='کشور ')),
                ('state', models.CharField(blank=True, max_length=255, null=True, verbose_name='استان ')),
                ('city', models.CharField(blank=True, max_length=255, null=True, verbose_name='شهر ')),
                ('zip_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='کدپستی ')),
                ('about', models.TextField(blank=True, null=True, verbose_name='درباره ')),
                ('contact_details', models.TextField(blank=True, null=True, verbose_name='جزییات اطلاعات تماس ')),
                ('latitude', models.CharField(blank=True, max_length=512, null=True, verbose_name='عرض جغرافیایی ')),
                ('longitude', models.CharField(blank=True, max_length=512, null=True, verbose_name='طول جغرافیایی ')),
                ('year_established', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='سال تاسیس ')),
                ('total_employees', models.CharField(blank=True, max_length=255, null=True, verbose_name='تعداد کارمندان ')),
                ('business_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='نوع تجارت ')),
                ('main_products', models.CharField(blank=True, max_length=255, null=True, verbose_name='محصولات اصلی ')),
                ('total_annual_revenue', models.CharField(blank=True, max_length=255, null=True, verbose_name='سود خالص سالانه ')),
                ('url', models.CharField(blank=True, max_length=255, null=True, verbose_name='لینک ')),
                ('social_link', models.CharField(blank=True, max_length=255, null=True, verbose_name='لینک شبکه ی اجتماعی ')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='utility.company', verbose_name='کمپانی ')),
            ],
            options={
                'verbose_name': 'شاخه ی کمپانی',
                'verbose_name_plural': 'شاخ های کمپانی',
            },
        ),
    ]
