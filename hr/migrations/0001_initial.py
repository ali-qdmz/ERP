# Generated by Django 3.2.5 on 2021-09-04 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='نام ')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='نام خانوادگی ')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=32, verbose_name='جنسیت ')),
                ('date_of_birth', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='تاریخ تولد ')),
                ('nationalid', models.CharField(blank=True, max_length=255, null=True, verbose_name='کئ ملی ')),
                ('blood_group', models.CharField(blank=True, max_length=255, null=True, verbose_name='گروه خونی ')),
                ('marital_status', models.CharField(blank=True, max_length=255, null=True, verbose_name='وضعیت نظام وظیفه ')),
                ('name_spouse', models.CharField(blank=True, max_length=255, null=True, verbose_name='نام همسر ')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='ایمیل ')),
                ('cell_phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='شماره تماس همراه ')),
                ('land_phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='شماره تماس ثابت ')),
                ('country', models.CharField(blank=True, choices=[('NLD', 'Netherlands'), ('DEU', 'Germany'), ('FRA', 'France'), ('BRA', 'Brazil'), ('USA', 'United States'), ('ABW', 'Aruba'), ('AFG', 'Afghanistan'), ('AGO', 'Angola'), ('AIA', 'Anguilla'), ('ALA', 'Aland Islands'), ('ALB', 'Albania'), ('AND', 'Andorra'), ('ANT', 'Netherlands Antilles'), ('ARE', 'United Arab Emirates'), ('ARG', 'Argentina'), ('ARM', 'Armenia'), ('ASM', 'American Samoa'), ('ATA', 'Antarctica'), ('ATF', 'French Southern Territories'), ('ATG', 'Antigua and Barbuda'), ('AUS', 'Australia'), ('AUT', 'Austria'), ('AZE', 'Azerbaijan'), ('BDI', 'Burundi'), ('BEL', 'Belgium'), ('BEN', 'Benin'), ('BFA', 'Burkina Faso'), ('BGD', 'Bangladesh'), ('BGR', 'Bulgaria'), ('BHR', 'Bahrain'), ('BHS', 'Bahamas'), ('BIH', 'Bosnia and Herzegovina'), ('BLM', 'Saint Barthelemy'), ('BLR', 'Belarus'), ('BLZ', 'Belize'), ('BMU', 'Bermuda'), ('BOL', 'Bolivia, Plurinational State of'), ('BRB', 'Barbados'), ('BRN', 'Brunei Darussalam'), ('BTN', 'Bhutan'), ('BVT', 'Bouvet Island'), ('BWA', 'Botswana'), ('CAF', 'Central African Republic'), ('CAN', 'Canada'), ('CCK', 'Cocos (Keeling) Islands'), ('CHE', 'Switzerland'), ('CHL', 'Chile'), ('CHN', 'China'), ('CIV', "Cote d'Ivoire"), ('CMR', 'Cameroon'), ('COD', 'Congo, the Democratic Republic of the'), ('COG', 'Congo'), ('COK', 'Cook Islands'), ('COL', 'Colombia'), ('COM', 'Comoros'), ('CPV', 'Cape Verde'), ('CRI', 'Costa Rica'), ('CUB', 'Cuba'), ('CXR', 'Christmas Island'), ('CYM', 'Cayman Islands'), ('CYP', 'Cyprus'), ('CZE', 'Czech Republic'), ('DJI', 'Djibouti'), ('DMA', 'Dominica'), ('DNK', 'Denmark'), ('DOM', 'Dominican Republic'), ('DZA', 'Algeria'), ('ECU', 'Ecuador'), ('EGY', 'Egypt'), ('ERI', 'Eritrea'), ('ESH', 'Western Sahara'), ('ESP', 'Spain'), ('EST', 'Estonia'), ('ETH', 'Ethiopia'), ('FIN', 'Finland'), ('FJI', 'Fiji'), ('FLK', 'Falkland Islands (Malvinas)'), ('FRO', 'Faroe Islands'), ('FSM', 'Micronesia, Federated States of'), ('GAB', 'Gabon'), ('GBR', 'United Kingdom'), ('GEO', 'Georgia'), ('GGY', 'Guernsey'), ('GHA', 'Ghana'), ('GIB', 'Gibraltar'), ('GIN', 'Guinea'), ('GLP', 'Guadeloupe'), ('GMB', 'Gambia'), ('GNB', 'Guinea-Bissau'), ('GNQ', 'Equatorial Guinea'), ('GRC', 'Greece'), ('GRD', 'Grenada'), ('GRL', 'Greenland'), ('GTM', 'Guatemala'), ('GUF', 'French Guiana'), ('GUM', 'Guam'), ('GUY', 'Guyana'), ('HKG', 'Hong Kong'), ('HMD', 'Heard Island and McDonald Islands'), ('HND', 'Honduras'), ('HRV', 'Croatia'), ('HTI', 'Haiti'), ('HUN', 'Hungary'), ('IDN', 'Indonesia'), ('IMN', 'Isle of Man'), ('IND', 'India'), ('IOT', 'British Indian Ocean Territory'), ('IRL', 'Ireland'), ('IRN', 'Iran, Islamic Republic of'), ('IRQ', 'Iraq'), ('ISL', 'Iceland'), ('ISR', 'Israel'), ('ITA', 'Italy'), ('JAM', 'Jamaica'), ('JEY', 'Jersey'), ('JOR', 'Jordan'), ('JPN', 'Japan'), ('KAZ', 'Kazakhstan'), ('KEN', 'Kenya'), ('KGZ', 'Kyrgyzstan'), ('KHM', 'Cambodia'), ('KIR', 'Kiribati'), ('KNA', 'Saint Kitts and Nevis'), ('KOR', 'Korea, Republic of'), ('KWT', 'Kuwait'), ('LAO', "Lao People's Democratic Republic"), ('LBN', 'Lebanon'), ('LBR', 'Liberia'), ('LBY', 'Libyan Arab Jamahiriya'), ('LCA', 'Saint Lucia'), ('LIE', 'Liechtenstein'), ('LKA', 'Sri Lanka'), ('LSO', 'Lesotho'), ('LTU', 'Lithuania'), ('LUX', 'Luxembourg'), ('LVA', 'Latvia'), ('MAC', 'Macao'), ('MAF', 'Saint Martin (French part)'), ('MAR', 'Morocco'), ('MCO', 'Monaco'), ('MDA', 'Moldova, Republic of'), ('MDG', 'Madagascar'), ('MDV', 'Maldives'), ('MEX', 'Mexico'), ('MHL', 'Marshall Islands'), ('MKD', 'Macedonia, the former Yugoslav Republic of'), ('MLI', 'Mali'), ('MLT', 'Malta'), ('MMR', 'Myanmar'), ('MNE', 'Montenegro'), ('MNG', 'Mongolia'), ('MNP', 'Northern Mariana Islands'), ('MOZ', 'Mozambique'), ('MRT', 'Mauritania'), ('MSR', 'Montserrat'), ('MTQ', 'Martinique'), ('MUS', 'Mauritius'), ('MWI', 'Malawi'), ('MYS', 'Malaysia'), ('MYT', 'Mayotte'), ('NAM', 'Namibia'), ('NCL', 'New Caledonia'), ('NER', 'Niger'), ('NFK', 'Norfolk Island'), ('NGA', 'Nigeria'), ('NIC', 'Nicaragua'), ('NIU', 'Niue'), ('NOR', 'Norway'), ('NPL', 'Nepal'), ('NRU', 'Nauru'), ('NZL', 'New Zealand'), ('OMN', 'Oman'), ('PAK', 'Pakistan'), ('PAN', 'Panama'), ('PCN', 'Pitcairn'), ('PER', 'Peru'), ('PHL', 'Philippines'), ('PLW', 'Palau'), ('PNG', 'Papua New Guinea'), ('POL', 'Poland'), ('PRI', 'Puerto Rico'), ('PRK', 'North Korea'), ('PRT', 'Portugal'), ('PRY', 'Paraguay'), ('PSE', 'Palestinian Territory, Occupied'), ('PYF', 'French Polynesia'), ('QAT', 'Qatar'), ('REU', 'Reunion'), ('ROU', 'Romania'), ('RUS', 'Russian Federation'), ('RWA', 'Rwanda'), ('SAU', 'Saudi Arabia'), ('SDN', 'Sudan'), ('SEN', 'Senegal'), ('SGP', 'Singapore'), ('SGS', 'South Georgia and the South Sandwich Islands'), ('SHN', 'Saint Helena, Ascension and Tristan da Cunha'), ('SJM', 'Svalbard and Jan Mayen'), ('SLB', 'Solomon Islands'), ('SLE', 'Sierra Leone'), ('SLV', 'El Salvador'), ('SMR', 'San Marino'), ('SOM', 'Somalia'), ('SPM', 'Saint Pierre and Miquelon'), ('SRB', 'Serbia'), ('STP', 'Sao Tome and Principe'), ('SUR', 'Suriname'), ('SVK', 'Slovakia'), ('SVN', 'Slovenia'), ('SWE', 'Sweden'), ('SWZ', 'Swaziland'), ('SYC', 'Seychelles'), ('SYR', 'Syrian Arab Republic'), ('TCA', 'Turks and Caicos Islands'), ('TCD', 'Chad'), ('TGO', 'Togo'), ('THA', 'Thailand'), ('TJK', 'Tajikistan'), ('TKL', 'Tokelau'), ('TKM', 'Turkmenistan'), ('TLS', 'Timor-Leste'), ('TON', 'Tonga'), ('TTO', 'Trinidad and Tobago'), ('TUN', 'Tunisia'), ('TUR', 'Turkey'), ('TUV', 'Tuvalu'), ('TWN', 'Taiwan, Province of China'), ('TZA', 'Tanzania, United Republic of'), ('UGA', 'Uganda'), ('UKR', 'Ukraine'), ('UMI', 'United States Minor Outlying Islands'), ('URY', 'Uruguay'), ('UZB', 'Uzbekistan'), ('VAT', 'Holy See (Vatican City State)'), ('VCT', 'Saint Vincent and the Grenadines'), ('VEN', 'Venezuela, Bolivarian Republic of'), ('VGB', 'Virgin Islands, British'), ('VIR', 'Virgin Islands, U.S.'), ('VNM', 'Viet Nam'), ('VUT', 'Vanuatu'), ('WLF', 'Wallis and Futuna'), ('WSM', 'Samoa'), ('YEM', 'Yemen'), ('ZAF', 'South Africa'), ('ZMB', 'Zambia'), ('ZWE', 'Zimbabwe')], max_length=32, verbose_name='کشور ')),
                ('state', models.CharField(blank=True, max_length=255, null=True, verbose_name='استان ')),
                ('city', models.CharField(blank=True, max_length=255, null=True, verbose_name='شهر ')),
                ('zip_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='کدپستی ')),
                ('permanent_address', models.TextField(blank=True, null=True, verbose_name='نام ')),
                ('about', models.TextField(blank=True, null=True, verbose_name='درباره ')),
                ('contact_details', models.TextField(blank=True, null=True, verbose_name='جزییات اطلاعات تماس ')),
                ('latitude', models.CharField(blank=True, max_length=512, null=True, verbose_name='عرض جغرافیایی ')),
                ('longitude', models.CharField(blank=True, max_length=512, null=True, verbose_name='طول جغرافیایی ')),
                ('personal_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='کد پرسنلی ')),
                ('fathers_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='نام پدر ')),
                ('mothers_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='نام مادر ')),
                ('home_district', models.CharField(blank=True, max_length=255, null=True, verbose_name='منطقه ی منزل ')),
                ('spouse_occupation', models.CharField(blank=True, max_length=255, null=True, verbose_name='وضعیت تاهل ')),
                ('spouse_district', models.CharField(blank=True, max_length=255, null=True, verbose_name='منطقه ی منزل همسر ')),
                ('religion', models.CharField(blank=True, max_length=255, null=True, verbose_name='دین ')),
                ('date_joining', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='تاریخ پیوستن ')),
                ('entry_designation', models.CharField(blank=True, max_length=255, null=True, verbose_name='نقش هنگام ورود ')),
                ('entry_scale', models.CharField(blank=True, max_length=255, null=True, verbose_name='مقیاس ورود ')),
                ('picture', models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d', verbose_name='ورود ')),
                ('archive_status', models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=32, verbose_name='وضعیت بایگانی ')),
                ('status', models.CharField(blank=True, choices=[('active', 'active'), ('inactive', 'inactive')], max_length=32, verbose_name='وضعیت ')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Employee', to=settings.AUTH_USER_MODEL, verbose_name='کاربر ')),
            ],
            options={
                'verbose_name': 'کارمند',
                'verbose_name_plural': 'کارمندان',
            },
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_trainin', models.CharField(blank=True, max_length=255, null=True, verbose_name='عنوان آموزش ')),
                ('institution', models.CharField(blank=True, max_length=255, null=True, verbose_name='موسسه ')),
                ('date_from', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='از تازیخ ')),
                ('date_to', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='تا تاریخ ')),
                ('trining_type', models.CharField(blank=True, choices=[('داخلی', 'داخلی'), ('خارجی', 'خارجی')], max_length=32, verbose_name='نوع آموزش ')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Training', to='hr.employee', verbose_name='کارمند ')),
            ],
            options={
                'verbose_name': 'گواهی نامه',
                'verbose_name_plural': 'گواهی نامه ها',
            },
        ),
        migrations.CreateModel(
            name='ServiceHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(blank=True, max_length=255, null=True, verbose_name='نقش ')),
                ('office_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='ساعت اداری ')),
                ('section', models.CharField(blank=True, max_length=255, null=True, verbose_name='بخش ')),
                ('date_from', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='از تاریخ ')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ServiceHistory', to='hr.employee', verbose_name='کارمند ')),
            ],
            options={
                'verbose_name': 'تاریخچه ی خدمت',
                'verbose_name_plural': 'تاریخچه های خدمت',
            },
        ),
        migrations.CreateModel(
            name='Retirement_year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='سال ')),
                ('date', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='تاریخ ')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Retirement_year', to='hr.employee', verbose_name='کارمند ')),
            ],
            options={
                'verbose_name': 'تاریخ بازنشستگی',
                'verbose_name_plural': 'تاریخ های بازنشستگی',
            },
        ),
        migrations.CreateModel(
            name='Rest_of_recreation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='از تاریخ ')),
                ('coming_date', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='تا تاریخ ')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Rest_of_recreation', to='hr.employee', verbose_name='کارمند ')),
            ],
            options={
                'verbose_name': 'کارمند',
                'verbose_name_plural': 'کارمندان',
            },
        ),
        migrations.CreateModel(
            name='Promotions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_promotion', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='تاریخ ارتقا ')),
                ('designation', models.CharField(blank=True, max_length=255, null=True, verbose_name='نقش ')),
                ('pay_scale', models.CharField(blank=True, max_length=255, null=True, verbose_name='اشل حقوقی ')),
                ('nature_promotion', models.CharField(blank=True, max_length=255, null=True, verbose_name='نوع ارتقا ')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Promotions', to='hr.employee', verbose_name='کارمند ')),
            ],
            options={
                'verbose_name': 'ارتقا',
                'verbose_name_plural': 'ارتقا ها',
            },
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('languages', models.CharField(blank=True, max_length=255, null=True, verbose_name='زبان ')),
                ('read', models.CharField(blank=True, max_length=255, null=True, verbose_name='خواندن ')),
                ('write', models.CharField(blank=True, max_length=255, null=True, verbose_name='نوشتن ')),
                ('speak', models.CharField(blank=True, max_length=255, null=True, verbose_name='مکالمه ')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Languages', to='hr.employee', verbose_name='کارمند ')),
            ],
            options={
                'verbose_name': 'زبان',
                'verbose_name_plural': 'زبان ها',
            },
        ),
        migrations.CreateModel(
            name='Employee_Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات ')),
                ('no_of_units_completed', models.DecimalField(decimal_places=2, default='0.00', max_digits=12, verbose_name='شماره واحد هایی که کامل کرده ')),
                ('points_on_unit_task', models.DecimalField(decimal_places=2, default='0.00', max_digits=12, verbose_name='امتیاز واحد عملیات ')),
                ('total_units_points', models.DecimalField(decimal_places=2, default='0.00', max_digits=12, verbose_name='جمع امتیازات ')),
                ('date_achivement', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='تاریخ موفقیت ')),
                ('points_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ManagerAchievement', to='hr.employee', verbose_name='امتیاز داده می شود با ')),
                ('points_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='EmployeeAchievement', to='hr.employee', verbose_name='امتیاز داده می شود به ')),
            ],
            options={
                'verbose_name': 'موفقیت کارمند',
                'verbose_name_plural': 'موفقیت های کارمند',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_institution', models.CharField(blank=True, max_length=255, null=True, verbose_name='نام موسسه ')),
                ('principals_subject', models.CharField(blank=True, max_length=255, null=True, verbose_name='موضوعات اصلی ')),
                ('degree', models.CharField(blank=True, max_length=255, null=True, verbose_name='درجه ')),
                ('year', models.CharField(blank=True, max_length=255, null=True, verbose_name='سال ')),
                ('division', models.CharField(blank=True, max_length=255, null=True, verbose_name='گرایش ')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Education', to='hr.employee', verbose_name='کارمند ')),
            ],
            options={
                'verbose_name': 'تحصیلات',
                'verbose_name_plural': 'تحصیلات ها',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='نام ')),
                ('status', models.CharField(blank=True, choices=[('active', 'active'), ('inactive', 'inactive')], max_length=32, verbose_name='وضعیت ')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='District', to='hr.employee', verbose_name='کارمند ')),
            ],
            options={
                'verbose_name': 'ناحیه',
                'verbose_name_plural': 'ناحیه ها',
            },
        ),
        migrations.CreateModel(
            name='DisciplinaryAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nature_offence', models.CharField(blank=True, max_length=255, null=True, verbose_name='سو پیشینه ')),
                ('punishment', models.CharField(blank=True, max_length=255, null=True, verbose_name='مجازات ')),
                ('date', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='تاریخ ')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='DisciplinaryAction', to='hr.employee', verbose_name='کارمند ')),
            ],
            options={
                'verbose_name': 'سو پیشینه',
                'verbose_name_plural': 'سو پیشینه ها',
            },
        ),
        migrations.CreateModel(
            name='Children',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='نام ')),
                ('sex', models.CharField(blank=True, choices=[('مرد', 'مرد'), ('زن', 'زن'), ('دیگر', 'دیگر')], max_length=32, verbose_name='جنسیت ')),
                ('dob', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='تاریخ تولد ')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Children', to='hr.employee', verbose_name='کارمند ')),
            ],
            options={
                'verbose_name': 'فرزند',
                'verbose_name_plural': 'فرزندان',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('road_village', models.CharField(blank=True, max_length=255, null=True, verbose_name='خیابان ')),
                ('postoffice', models.CharField(blank=True, max_length=255, null=True, verbose_name='اداره پست ')),
                ('post_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='کد پستی ')),
                ('flat_no', models.CharField(blank=True, max_length=255, null=True, verbose_name='آپارتمان ')),
                ('police_station_thana', models.CharField(blank=True, max_length=255, null=True, verbose_name='اداره ی پلیس ')),
                ('district', models.CharField(blank=True, max_length=255, null=True, verbose_name='ناحیه ')),
                ('date_from', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='از تاریخ ')),
                ('address_type', models.CharField(blank=True, choices=[('موقتی', 'موقتی'), ('دایمی', 'دایمی')], max_length=32, verbose_name='نوع آدرس ')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Address', to='hr.employee', verbose_name='کارمند ')),
            ],
            options={
                'verbose_name': 'آدرس',
                'verbose_name_plural': 'آدرس ها',
            },
        ),
    ]