# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 04:46
from __future__ import unicode_literals

import apps.profiles.fields
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.ASCIIUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('featured', models.BooleanField(default=False)),
                ('bio', models.TextField(blank=True)),
                ('twitter_username', models.CharField(blank=True, max_length=50)),
                ('facebook_username', models.CharField(blank=True, max_length=50)),
                ('github_username', models.CharField(blank=True, max_length=50)),
                ('linkedin_url', models.URLField(blank=True)),
                ('website_url', models.URLField(blank=True)),
                ('gravatar_url', models.URLField(blank=True)),
                ('is_gravatar_verified', models.BooleanField(default=False)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('state', models.CharField(blank=True, max_length=50)),
                ('day_of_week', apps.profiles.fields.DaysOfWeekField(blank=True, choices=[(0, 'Lunes'), (1, 'Martes'), (2, 'Mi\xe9rcoles'), (3, 'Jueves'), (4, 'Viernes'), (5, 'S\xe1bado'), (6, 'Domingo')], db_index=True, null=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('timezone', models.CharField(choices=[(b'', '--- Selecciona ---'), (b'Africa/Abidjan', b'Africa/Abidjan (GMT +0000)'), (b'Africa/Accra', b'Africa/Accra (GMT +0000)'), (b'Africa/Addis_Ababa', b'Africa/Addis_Ababa (GMT +0300)'), (b'Africa/Algiers', b'Africa/Algiers (GMT +0100)'), (b'Africa/Asmara', b'Africa/Asmara (GMT +0300)'), (b'Africa/Bamako', b'Africa/Bamako (GMT +0000)'), (b'Africa/Bangui', b'Africa/Bangui (GMT +0100)'), (b'Africa/Banjul', b'Africa/Banjul (GMT +0000)'), (b'Africa/Bissau', b'Africa/Bissau (GMT +0000)'), (b'Africa/Blantyre', b'Africa/Blantyre (GMT +0200)'), (b'Africa/Brazzaville', b'Africa/Brazzaville (GMT +0100)'), (b'Africa/Bujumbura', b'Africa/Bujumbura (GMT +0200)'), (b'Africa/Cairo', b'Africa/Cairo (GMT +0200)'), (b'Africa/Casablanca', b'Africa/Casablanca (GMT +0000)'), (b'Africa/Ceuta', b'Africa/Ceuta (GMT +0100)'), (b'Africa/Conakry', b'Africa/Conakry (GMT +0000)'), (b'Africa/Dakar', b'Africa/Dakar (GMT +0000)'), (b'Africa/Dar_es_Salaam', b'Africa/Dar_es_Salaam (GMT +0300)'), (b'Africa/Djibouti', b'Africa/Djibouti (GMT +0300)'), (b'Africa/Douala', b'Africa/Douala (GMT +0100)'), (b'Africa/El_Aaiun', b'Africa/El_Aaiun (GMT +0000)'), (b'Africa/Freetown', b'Africa/Freetown (GMT +0000)'), (b'Africa/Gaborone', b'Africa/Gaborone (GMT +0200)'), (b'Africa/Harare', b'Africa/Harare (GMT +0200)'), (b'Africa/Johannesburg', b'Africa/Johannesburg (GMT +0200)'), (b'Africa/Juba', b'Africa/Juba (GMT +0300)'), (b'Africa/Kampala', b'Africa/Kampala (GMT +0300)'), (b'Africa/Khartoum', b'Africa/Khartoum (GMT +0300)'), (b'Africa/Kigali', b'Africa/Kigali (GMT +0200)'), (b'Africa/Kinshasa', b'Africa/Kinshasa (GMT +0100)'), (b'Africa/Lagos', b'Africa/Lagos (GMT +0100)'), (b'Africa/Libreville', b'Africa/Libreville (GMT +0100)'), (b'Africa/Lome', b'Africa/Lome (GMT +0000)'), (b'Africa/Luanda', b'Africa/Luanda (GMT +0100)'), (b'Africa/Lubumbashi', b'Africa/Lubumbashi (GMT +0200)'), (b'Africa/Lusaka', b'Africa/Lusaka (GMT +0200)'), (b'Africa/Malabo', b'Africa/Malabo (GMT +0100)'), (b'Africa/Maputo', b'Africa/Maputo (GMT +0200)'), (b'Africa/Maseru', b'Africa/Maseru (GMT +0200)'), (b'Africa/Mbabane', b'Africa/Mbabane (GMT +0200)'), (b'Africa/Mogadishu', b'Africa/Mogadishu (GMT +0300)'), (b'Africa/Monrovia', b'Africa/Monrovia (GMT +0000)'), (b'Africa/Nairobi', b'Africa/Nairobi (GMT +0300)'), (b'Africa/Ndjamena', b'Africa/Ndjamena (GMT +0100)'), (b'Africa/Niamey', b'Africa/Niamey (GMT +0100)'), (b'Africa/Nouakchott', b'Africa/Nouakchott (GMT +0000)'), (b'Africa/Ouagadougou', b'Africa/Ouagadougou (GMT +0000)'), (b'Africa/Porto-Novo', b'Africa/Porto-Novo (GMT +0100)'), (b'Africa/Sao_Tome', b'Africa/Sao_Tome (GMT +0000)'), (b'Africa/Tripoli', b'Africa/Tripoli (GMT +0200)'), (b'Africa/Tunis', b'Africa/Tunis (GMT +0100)'), (b'Africa/Windhoek', b'Africa/Windhoek (GMT +0200)'), (b'America/Adak', b'America/Adak (GMT -0900)'), (b'America/Anchorage', b'America/Anchorage (GMT -0800)'), (b'America/Anguilla', b'America/Anguilla (GMT -0400)'), (b'America/Antigua', b'America/Antigua (GMT -0400)'), (b'America/Araguaina', b'America/Araguaina (GMT -0300)'), (b'America/Argentina/Buenos_Aires', b'America/Argentina/Buenos_Aires (GMT -0300)'), (b'America/Argentina/Catamarca', b'America/Argentina/Catamarca (GMT -0300)'), (b'America/Argentina/Cordoba', b'America/Argentina/Cordoba (GMT -0300)'), (b'America/Argentina/Jujuy', b'America/Argentina/Jujuy (GMT -0300)'), (b'America/Argentina/La_Rioja', b'America/Argentina/La_Rioja (GMT -0300)'), (b'America/Argentina/Mendoza', b'America/Argentina/Mendoza (GMT -0300)'), (b'America/Argentina/Rio_Gallegos', b'America/Argentina/Rio_Gallegos (GMT -0300)'), (b'America/Argentina/Salta', b'America/Argentina/Salta (GMT -0300)'), (b'America/Argentina/San_Juan', b'America/Argentina/San_Juan (GMT -0300)'), (b'America/Argentina/San_Luis', b'America/Argentina/San_Luis (GMT -0300)'), (b'America/Argentina/Tucuman', b'America/Argentina/Tucuman (GMT -0300)'), (b'America/Argentina/Ushuaia', b'America/Argentina/Ushuaia (GMT -0300)'), (b'America/Aruba', b'America/Aruba (GMT -0400)'), (b'America/Asuncion', b'America/Asuncion (GMT -0300)'), (b'America/Atikokan', b'America/Atikokan (GMT -0500)'), (b'America/Bahia', b'America/Bahia (GMT -0300)'), (b'America/Bahia_Banderas', b'America/Bahia_Banderas (GMT -0600)'), (b'America/Barbados', b'America/Barbados (GMT -0400)'), (b'America/Belem', b'America/Belem (GMT -0300)'), (b'America/Belize', b'America/Belize (GMT -0600)'), (b'America/Blanc-Sablon', b'America/Blanc-Sablon (GMT -0400)'), (b'America/Boa_Vista', b'America/Boa_Vista (GMT -0400)'), (b'America/Bogota', b'America/Bogota (GMT -0500)'), (b'America/Boise', b'America/Boise (GMT -0600)'), (b'America/Cambridge_Bay', b'America/Cambridge_Bay (GMT -0600)'), (b'America/Campo_Grande', b'America/Campo_Grande (GMT -0400)'), (b'America/Cancun', b'America/Cancun (GMT -0600)'), (b'America/Caracas', b'America/Caracas (GMT -0430)'), (b'America/Cayenne', b'America/Cayenne (GMT -0300)'), (b'America/Cayman', b'America/Cayman (GMT -0500)'), (b'America/Chicago', b'America/Chicago (GMT -0500)'), (b'America/Chihuahua', b'America/Chihuahua (GMT -0700)'), (b'America/Costa_Rica', b'America/Costa_Rica (GMT -0600)'), (b'America/Creston', b'America/Creston (GMT -0700)'), (b'America/Cuiaba', b'America/Cuiaba (GMT -0400)'), (b'America/Curacao', b'America/Curacao (GMT -0400)'), (b'America/Danmarkshavn', b'America/Danmarkshavn (GMT +0000)'), (b'America/Dawson', b'America/Dawson (GMT -0700)'), (b'America/Dawson_Creek', b'America/Dawson_Creek (GMT -0700)'), (b'America/Denver', b'America/Denver (GMT -0600)'), (b'America/Detroit', b'America/Detroit (GMT -0400)'), (b'America/Dominica', b'America/Dominica (GMT -0400)'), (b'America/Edmonton', b'America/Edmonton (GMT -0600)'), (b'America/Eirunepe', b'America/Eirunepe (GMT -0500)'), (b'America/El_Salvador', b'America/El_Salvador (GMT -0600)'), (b'America/Fortaleza', b'America/Fortaleza (GMT -0300)'), (b'America/Glace_Bay', b'America/Glace_Bay (GMT -0300)'), (b'America/Godthab', b'America/Godthab (GMT -0300)'), (b'America/Goose_Bay', b'America/Goose_Bay (GMT -0300)'), (b'America/Grand_Turk', b'America/Grand_Turk (GMT -0400)'), (b'America/Grenada', b'America/Grenada (GMT -0400)'), (b'America/Guadeloupe', b'America/Guadeloupe (GMT -0400)'), (b'America/Guatemala', b'America/Guatemala (GMT -0600)'), (b'America/Guayaquil', b'America/Guayaquil (GMT -0500)'), (b'America/Guyana', b'America/Guyana (GMT -0400)'), (b'America/Halifax', b'America/Halifax (GMT -0300)'), (b'America/Havana', b'America/Havana (GMT -0400)'), (b'America/Hermosillo', b'America/Hermosillo (GMT -0700)'), (b'America/Indiana/Indianapolis', b'America/Indiana/Indianapolis (GMT -0400)'), (b'America/Indiana/Knox', b'America/Indiana/Knox (GMT -0500)'), (b'America/Indiana/Marengo', b'America/Indiana/Marengo (GMT -0400)'), (b'America/Indiana/Petersburg', b'America/Indiana/Petersburg (GMT -0400)'), (b'America/Indiana/Tell_City', b'America/Indiana/Tell_City (GMT -0500)'), (b'America/Indiana/Vevay', b'America/Indiana/Vevay (GMT -0400)'), (b'America/Indiana/Vincennes', b'America/Indiana/Vincennes (GMT -0400)'), (b'America/Indiana/Winamac', b'America/Indiana/Winamac (GMT -0400)'), (b'America/Inuvik', b'America/Inuvik (GMT -0600)'), (b'America/Iqaluit', b'America/Iqaluit (GMT -0400)'), (b'America/Jamaica', b'America/Jamaica (GMT -0500)'), (b'America/Juneau', b'America/Juneau (GMT -0800)'), (b'America/Kentucky/Louisville', b'America/Kentucky/Louisville (GMT -0400)'), (b'America/Kentucky/Monticello', b'America/Kentucky/Monticello (GMT -0400)'), (b'America/Kralendijk', b'America/Kralendijk (GMT -0400)'), (b'America/La_Paz', b'America/La_Paz (GMT -0400)'), (b'America/Lima', b'America/Lima (GMT -0500)'), (b'America/Los_Angeles', b'America/Los_Angeles (GMT -0700)'), (b'America/Lower_Princes', b'America/Lower_Princes (GMT -0400)'), (b'America/Maceio', b'America/Maceio (GMT -0300)'), (b'America/Managua', b'America/Managua (GMT -0600)'), (b'America/Manaus', b'America/Manaus (GMT -0400)'), (b'America/Marigot', b'America/Marigot (GMT -0400)'), (b'America/Martinique', b'America/Martinique (GMT -0400)'), (b'America/Matamoros', b'America/Matamoros (GMT -0500)'), (b'America/Mazatlan', b'America/Mazatlan (GMT -0700)'), (b'America/Menominee', b'America/Menominee (GMT -0500)'), (b'America/Merida', b'America/Merida (GMT -0600)'), (b'America/Metlakatla', b'America/Metlakatla (GMT -0800)'), (b'America/Mexico_City', b'America/Mexico_City (GMT -0600)'), (b'America/Miquelon', b'America/Miquelon (GMT -0200)'), (b'America/Moncton', b'America/Moncton (GMT -0300)'), (b'America/Monterrey', b'America/Monterrey (GMT -0600)'), (b'America/Montevideo', b'America/Montevideo (GMT -0300)'), (b'America/Montreal', b'America/Montreal (GMT -0400)'), (b'America/Montserrat', b'America/Montserrat (GMT -0400)'), (b'America/Nassau', b'America/Nassau (GMT -0400)'), (b'America/New_York', b'America/New_York (GMT -0400)'), (b'America/Nipigon', b'America/Nipigon (GMT -0400)'), (b'America/Nome', b'America/Nome (GMT -0800)'), (b'America/Noronha', b'America/Noronha (GMT -0200)'), (b'America/North_Dakota/Beulah', b'America/North_Dakota/Beulah (GMT -0500)'), (b'America/North_Dakota/Center', b'America/North_Dakota/Center (GMT -0500)'), (b'America/North_Dakota/New_Salem', b'America/North_Dakota/New_Salem (GMT -0500)'), (b'America/Ojinaga', b'America/Ojinaga (GMT -0600)'), (b'America/Panama', b'America/Panama (GMT -0500)'), (b'America/Pangnirtung', b'America/Pangnirtung (GMT -0400)'), (b'America/Paramaribo', b'America/Paramaribo (GMT -0300)'), (b'America/Phoenix', b'America/Phoenix (GMT -0700)'), (b'America/Port-au-Prince', b'America/Port-au-Prince (GMT -0400)'), (b'America/Port_of_Spain', b'America/Port_of_Spain (GMT -0400)'), (b'America/Porto_Velho', b'America/Porto_Velho (GMT -0400)'), (b'America/Puerto_Rico', b'America/Puerto_Rico (GMT -0400)'), (b'America/Rainy_River', b'America/Rainy_River (GMT -0500)'), (b'America/Rankin_Inlet', b'America/Rankin_Inlet (GMT -0500)'), (b'America/Recife', b'America/Recife (GMT -0300)'), (b'America/Regina', b'America/Regina (GMT -0600)'), (b'America/Resolute', b'America/Resolute (GMT -0500)'), (b'America/Rio_Branco', b'America/Rio_Branco (GMT -0500)'), (b'America/Santa_Isabel', b'America/Santa_Isabel (GMT -0800)'), (b'America/Santarem', b'America/Santarem (GMT -0300)'), (b'America/Santiago', b'America/Santiago (GMT -0300)'), (b'America/Santo_Domingo', b'America/Santo_Domingo (GMT -0400)'), (b'America/Sao_Paulo', b'America/Sao_Paulo (GMT -0300)'), (b'America/Scoresbysund', b'America/Scoresbysund (GMT -0100)'), (b'America/Sitka', b'America/Sitka (GMT -0800)'), (b'America/St_Barthelemy', b'America/St_Barthelemy (GMT -0400)'), (b'America/St_Johns', b'America/St_Johns (GMT -0230)'), (b'America/St_Kitts', b'America/St_Kitts (GMT -0400)'), (b'America/St_Lucia', b'America/St_Lucia (GMT -0400)'), (b'America/St_Thomas', b'America/St_Thomas (GMT -0400)'), (b'America/St_Vincent', b'America/St_Vincent (GMT -0400)'), (b'America/Swift_Current', b'America/Swift_Current (GMT -0600)'), (b'America/Tegucigalpa', b'America/Tegucigalpa (GMT -0600)'), (b'America/Thule', b'America/Thule (GMT -0300)'), (b'America/Thunder_Bay', b'America/Thunder_Bay (GMT -0400)'), (b'America/Tijuana', b'America/Tijuana (GMT -0700)'), (b'America/Toronto', b'America/Toronto (GMT -0400)'), (b'America/Tortola', b'America/Tortola (GMT -0400)'), (b'America/Vancouver', b'America/Vancouver (GMT -0700)'), (b'America/Whitehorse', b'America/Whitehorse (GMT -0700)'), (b'America/Winnipeg', b'America/Winnipeg (GMT -0500)'), (b'America/Yakutat', b'America/Yakutat (GMT -0800)'), (b'America/Yellowknife', b'America/Yellowknife (GMT -0600)'), (b'Antarctica/Casey', b'Antarctica/Casey (GMT +0800)'), (b'Antarctica/Davis', b'Antarctica/Davis (GMT +0700)'), (b'Antarctica/DumontDUrville', b'Antarctica/DumontDUrville (GMT +1000)'), (b'Antarctica/Macquarie', b'Antarctica/Macquarie (GMT +1100)'), (b'Antarctica/Mawson', b'Antarctica/Mawson (GMT +0500)'), (b'Antarctica/McMurdo', b'Antarctica/McMurdo (GMT +1300)'), (b'Antarctica/Palmer', b'Antarctica/Palmer (GMT -0300)'), (b'Antarctica/Rothera', b'Antarctica/Rothera (GMT -0300)'), (b'Antarctica/Syowa', b'Antarctica/Syowa (GMT +0300)'), (b'Antarctica/Troll', b'Antarctica/Troll (GMT +0000)'), (b'Antarctica/Vostok', b'Antarctica/Vostok (GMT +0600)'), (b'Arctic/Longyearbyen', b'Arctic/Longyearbyen (GMT +0100)'), (b'Asia/Aden', b'Asia/Aden (GMT +0300)'), (b'Asia/Almaty', b'Asia/Almaty (GMT +0600)'), (b'Asia/Amman', b'Asia/Amman (GMT +0200)'), (b'Asia/Anadyr', b'Asia/Anadyr (GMT +1200)'), (b'Asia/Aqtau', b'Asia/Aqtau (GMT +0500)'), (b'Asia/Aqtobe', b'Asia/Aqtobe (GMT +0500)'), (b'Asia/Ashgabat', b'Asia/Ashgabat (GMT +0500)'), (b'Asia/Baghdad', b'Asia/Baghdad (GMT +0300)'), (b'Asia/Bahrain', b'Asia/Bahrain (GMT +0300)'), (b'Asia/Baku', b'Asia/Baku (GMT +0400)'), (b'Asia/Bangkok', b'Asia/Bangkok (GMT +0700)'), (b'Asia/Beirut', b'Asia/Beirut (GMT +0200)'), (b'Asia/Bishkek', b'Asia/Bishkek (GMT +0600)'), (b'Asia/Brunei', b'Asia/Brunei (GMT +0800)'), (b'Asia/Choibalsan', b'Asia/Choibalsan (GMT +0800)'), (b'Asia/Chongqing', b'Asia/Chongqing (GMT +0800)'), (b'Asia/Colombo', b'Asia/Colombo (GMT +0530)'), (b'Asia/Damascus', b'Asia/Damascus (GMT +0200)'), (b'Asia/Dhaka', b'Asia/Dhaka (GMT +0600)'), (b'Asia/Dili', b'Asia/Dili (GMT +0900)'), (b'Asia/Dubai', b'Asia/Dubai (GMT +0400)'), (b'Asia/Dushanbe', b'Asia/Dushanbe (GMT +0500)'), (b'Asia/Gaza', b'Asia/Gaza (GMT +0200)'), (b'Asia/Harbin', b'Asia/Harbin (GMT +0800)'), (b'Asia/Hebron', b'Asia/Hebron (GMT +0200)'), (b'Asia/Ho_Chi_Minh', b'Asia/Ho_Chi_Minh (GMT +0700)'), (b'Asia/Hong_Kong', b'Asia/Hong_Kong (GMT +0800)'), (b'Asia/Hovd', b'Asia/Hovd (GMT +0700)'), (b'Asia/Irkutsk', b'Asia/Irkutsk (GMT +0900)'), (b'Asia/Jakarta', b'Asia/Jakarta (GMT +0700)'), (b'Asia/Jayapura', b'Asia/Jayapura (GMT +0900)'), (b'Asia/Jerusalem', b'Asia/Jerusalem (GMT +0200)'), (b'Asia/Kabul', b'Asia/Kabul (GMT +0430)'), (b'Asia/Kamchatka', b'Asia/Kamchatka (GMT +1200)'), (b'Asia/Karachi', b'Asia/Karachi (GMT +0500)'), (b'Asia/Kashgar', b'Asia/Kashgar (GMT +0800)'), (b'Asia/Kathmandu', b'Asia/Kathmandu (GMT +0545)'), (b'Asia/Khandyga', b'Asia/Khandyga (GMT +1000)'), (b'Asia/Kolkata', b'Asia/Kolkata (GMT +0530)'), (b'Asia/Krasnoyarsk', b'Asia/Krasnoyarsk (GMT +0800)'), (b'Asia/Kuala_Lumpur', b'Asia/Kuala_Lumpur (GMT +0800)'), (b'Asia/Kuching', b'Asia/Kuching (GMT +0800)'), (b'Asia/Kuwait', b'Asia/Kuwait (GMT +0300)'), (b'Asia/Macau', b'Asia/Macau (GMT +0800)'), (b'Asia/Magadan', b'Asia/Magadan (GMT +1200)'), (b'Asia/Makassar', b'Asia/Makassar (GMT +0800)'), (b'Asia/Manila', b'Asia/Manila (GMT +0800)'), (b'Asia/Muscat', b'Asia/Muscat (GMT +0400)'), (b'Asia/Nicosia', b'Asia/Nicosia (GMT +0200)'), (b'Asia/Novokuznetsk', b'Asia/Novokuznetsk (GMT +0700)'), (b'Asia/Novosibirsk', b'Asia/Novosibirsk (GMT +0700)'), (b'Asia/Omsk', b'Asia/Omsk (GMT +0700)'), (b'Asia/Oral', b'Asia/Oral (GMT +0500)'), (b'Asia/Phnom_Penh', b'Asia/Phnom_Penh (GMT +0700)'), (b'Asia/Pontianak', b'Asia/Pontianak (GMT +0700)'), (b'Asia/Pyongyang', b'Asia/Pyongyang (GMT +0900)'), (b'Asia/Qatar', b'Asia/Qatar (GMT +0300)'), (b'Asia/Qyzylorda', b'Asia/Qyzylorda (GMT +0600)'), (b'Asia/Rangoon', b'Asia/Rangoon (GMT +0630)'), (b'Asia/Riyadh', b'Asia/Riyadh (GMT +0300)'), (b'Asia/Sakhalin', b'Asia/Sakhalin (GMT +1100)'), (b'Asia/Samarkand', b'Asia/Samarkand (GMT +0500)'), (b'Asia/Seoul', b'Asia/Seoul (GMT +0900)'), (b'Asia/Shanghai', b'Asia/Shanghai (GMT +0800)'), (b'Asia/Singapore', b'Asia/Singapore (GMT +0800)'), (b'Asia/Taipei', b'Asia/Taipei (GMT +0800)'), (b'Asia/Tashkent', b'Asia/Tashkent (GMT +0500)'), (b'Asia/Tbilisi', b'Asia/Tbilisi (GMT +0400)'), (b'Asia/Tehran', b'Asia/Tehran (GMT +0330)'), (b'Asia/Thimphu', b'Asia/Thimphu (GMT +0600)'), (b'Asia/Tokyo', b'Asia/Tokyo (GMT +0900)'), (b'Asia/Ulaanbaatar', b'Asia/Ulaanbaatar (GMT +0800)'), (b'Asia/Urumqi', b'Asia/Urumqi (GMT +0800)'), (b'Asia/Ust-Nera', b'Asia/Ust-Nera (GMT +1100)'), (b'Asia/Vientiane', b'Asia/Vientiane (GMT +0700)'), (b'Asia/Vladivostok', b'Asia/Vladivostok (GMT +1100)'), (b'Asia/Yakutsk', b'Asia/Yakutsk (GMT +1000)'), (b'Asia/Yekaterinburg', b'Asia/Yekaterinburg (GMT +0600)'), (b'Asia/Yerevan', b'Asia/Yerevan (GMT +0400)'), (b'Atlantic/Azores', b'Atlantic/Azores (GMT -0100)'), (b'Atlantic/Bermuda', b'Atlantic/Bermuda (GMT -0300)'), (b'Atlantic/Canary', b'Atlantic/Canary (GMT +0000)'), (b'Atlantic/Cape_Verde', b'Atlantic/Cape_Verde (GMT -0100)'), (b'Atlantic/Faroe', b'Atlantic/Faroe (GMT +0000)'), (b'Atlantic/Madeira', b'Atlantic/Madeira (GMT +0000)'), (b'Atlantic/Reykjavik', b'Atlantic/Reykjavik (GMT +0000)'), (b'Atlantic/South_Georgia', b'Atlantic/South_Georgia (GMT -0200)'), (b'Atlantic/St_Helena', b'Atlantic/St_Helena (GMT +0000)'), (b'Atlantic/Stanley', b'Atlantic/Stanley (GMT -0300)'), (b'Australia/Adelaide', b'Australia/Adelaide (GMT +1030)'), (b'Australia/Brisbane', b'Australia/Brisbane (GMT +1000)'), (b'Australia/Broken_Hill', b'Australia/Broken_Hill (GMT +1030)'), (b'Australia/Currie', b'Australia/Currie (GMT +1100)'), (b'Australia/Darwin', b'Australia/Darwin (GMT +0930)'), (b'Australia/Eucla', b'Australia/Eucla (GMT +0845)'), (b'Australia/Hobart', b'Australia/Hobart (GMT +1100)'), (b'Australia/Lindeman', b'Australia/Lindeman (GMT +1000)'), (b'Australia/Lord_Howe', b'Australia/Lord_Howe (GMT +1100)'), (b'Australia/Melbourne', b'Australia/Melbourne (GMT +1100)'), (b'Australia/Perth', b'Australia/Perth (GMT +0800)'), (b'Australia/Sydney', b'Australia/Sydney (GMT +1100)'), (b'Canada/Atlantic', b'Canada/Atlantic (GMT -0300)'), (b'Canada/Central', b'Canada/Central (GMT -0500)'), (b'Canada/Eastern', b'Canada/Eastern (GMT -0400)'), (b'Canada/Mountain', b'Canada/Mountain (GMT -0600)'), (b'Canada/Newfoundland', b'Canada/Newfoundland (GMT -0230)'), (b'Canada/Pacific', b'Canada/Pacific (GMT -0700)'), (b'Europe/Amsterdam', b'Europe/Amsterdam (GMT +0100)'), (b'Europe/Andorra', b'Europe/Andorra (GMT +0100)'), (b'Europe/Athens', b'Europe/Athens (GMT +0200)'), (b'Europe/Belgrade', b'Europe/Belgrade (GMT +0100)'), (b'Europe/Berlin', b'Europe/Berlin (GMT +0100)'), (b'Europe/Bratislava', b'Europe/Bratislava (GMT +0100)'), (b'Europe/Brussels', b'Europe/Brussels (GMT +0100)'), (b'Europe/Bucharest', b'Europe/Bucharest (GMT +0200)'), (b'Europe/Budapest', b'Europe/Budapest (GMT +0100)'), (b'Europe/Busingen', b'Europe/Busingen (GMT +0100)'), (b'Europe/Chisinau', b'Europe/Chisinau (GMT +0200)'), (b'Europe/Copenhagen', b'Europe/Copenhagen (GMT +0100)'), (b'Europe/Dublin', b'Europe/Dublin (GMT +0000)'), (b'Europe/Gibraltar', b'Europe/Gibraltar (GMT +0100)'), (b'Europe/Guernsey', b'Europe/Guernsey (GMT +0000)'), (b'Europe/Helsinki', b'Europe/Helsinki (GMT +0200)'), (b'Europe/Isle_of_Man', b'Europe/Isle_of_Man (GMT +0000)'), (b'Europe/Istanbul', b'Europe/Istanbul (GMT +0200)'), (b'Europe/Jersey', b'Europe/Jersey (GMT +0000)'), (b'Europe/Kaliningrad', b'Europe/Kaliningrad (GMT +0300)'), (b'Europe/Kiev', b'Europe/Kiev (GMT +0200)'), (b'Europe/Lisbon', b'Europe/Lisbon (GMT +0000)'), (b'Europe/Ljubljana', b'Europe/Ljubljana (GMT +0100)'), (b'Europe/London', b'Europe/London (GMT +0000)'), (b'Europe/Luxembourg', b'Europe/Luxembourg (GMT +0100)'), (b'Europe/Madrid', b'Europe/Madrid (GMT +0100)'), (b'Europe/Malta', b'Europe/Malta (GMT +0100)'), (b'Europe/Mariehamn', b'Europe/Mariehamn (GMT +0200)'), (b'Europe/Minsk', b'Europe/Minsk (GMT +0300)'), (b'Europe/Monaco', b'Europe/Monaco (GMT +0100)'), (b'Europe/Moscow', b'Europe/Moscow (GMT +0400)'), (b'Europe/Oslo', b'Europe/Oslo (GMT +0100)'), (b'Europe/Paris', b'Europe/Paris (GMT +0100)'), (b'Europe/Podgorica', b'Europe/Podgorica (GMT +0100)'), (b'Europe/Prague', b'Europe/Prague (GMT +0100)'), (b'Europe/Riga', b'Europe/Riga (GMT +0200)'), (b'Europe/Rome', b'Europe/Rome (GMT +0100)'), (b'Europe/Samara', b'Europe/Samara (GMT +0400)'), (b'Europe/San_Marino', b'Europe/San_Marino (GMT +0100)'), (b'Europe/Sarajevo', b'Europe/Sarajevo (GMT +0100)'), (b'Europe/Simferopol', b'Europe/Simferopol (GMT +0400)'), (b'Europe/Skopje', b'Europe/Skopje (GMT +0100)'), (b'Europe/Sofia', b'Europe/Sofia (GMT +0200)'), (b'Europe/Stockholm', b'Europe/Stockholm (GMT +0100)'), (b'Europe/Tallinn', b'Europe/Tallinn (GMT +0200)'), (b'Europe/Tirane', b'Europe/Tirane (GMT +0100)'), (b'Europe/Uzhgorod', b'Europe/Uzhgorod (GMT +0200)'), (b'Europe/Vaduz', b'Europe/Vaduz (GMT +0100)'), (b'Europe/Vatican', b'Europe/Vatican (GMT +0100)'), (b'Europe/Vienna', b'Europe/Vienna (GMT +0100)'), (b'Europe/Vilnius', b'Europe/Vilnius (GMT +0200)'), (b'Europe/Volgograd', b'Europe/Volgograd (GMT +0400)'), (b'Europe/Warsaw', b'Europe/Warsaw (GMT +0100)'), (b'Europe/Zagreb', b'Europe/Zagreb (GMT +0100)'), (b'Europe/Zaporozhye', b'Europe/Zaporozhye (GMT +0200)'), (b'Europe/Zurich', b'Europe/Zurich (GMT +0100)'), (b'GMT', b'GMT (GMT +0000)'), (b'Indian/Antananarivo', b'Indian/Antananarivo (GMT +0300)'), (b'Indian/Chagos', b'Indian/Chagos (GMT +0600)'), (b'Indian/Christmas', b'Indian/Christmas (GMT +0700)'), (b'Indian/Cocos', b'Indian/Cocos (GMT +0630)'), (b'Indian/Comoro', b'Indian/Comoro (GMT +0300)'), (b'Indian/Kerguelen', b'Indian/Kerguelen (GMT +0500)'), (b'Indian/Mahe', b'Indian/Mahe (GMT +0400)'), (b'Indian/Maldives', b'Indian/Maldives (GMT +0500)'), (b'Indian/Mauritius', b'Indian/Mauritius (GMT +0400)'), (b'Indian/Mayotte', b'Indian/Mayotte (GMT +0300)'), (b'Indian/Reunion', b'Indian/Reunion (GMT +0400)'), (b'Pacific/Apia', b'Pacific/Apia (GMT +1400)'), (b'Pacific/Auckland', b'Pacific/Auckland (GMT +1300)'), (b'Pacific/Chatham', b'Pacific/Chatham (GMT +1345)'), (b'Pacific/Chuuk', b'Pacific/Chuuk (GMT +1000)'), (b'Pacific/Easter', b'Pacific/Easter (GMT -0500)'), (b'Pacific/Efate', b'Pacific/Efate (GMT +1100)'), (b'Pacific/Enderbury', b'Pacific/Enderbury (GMT +1300)'), (b'Pacific/Fakaofo', b'Pacific/Fakaofo (GMT +1300)'), (b'Pacific/Fiji', b'Pacific/Fiji (GMT +1200)'), (b'Pacific/Funafuti', b'Pacific/Funafuti (GMT +1200)'), (b'Pacific/Galapagos', b'Pacific/Galapagos (GMT -0600)'), (b'Pacific/Gambier', b'Pacific/Gambier (GMT -0900)'), (b'Pacific/Guadalcanal', b'Pacific/Guadalcanal (GMT +1100)'), (b'Pacific/Guam', b'Pacific/Guam (GMT +1000)'), (b'Pacific/Honolulu', b'Pacific/Honolulu (GMT -1000)'), (b'Pacific/Johnston', b'Pacific/Johnston (GMT -1000)'), (b'Pacific/Kiritimati', b'Pacific/Kiritimati (GMT +1400)'), (b'Pacific/Kosrae', b'Pacific/Kosrae (GMT +1100)'), (b'Pacific/Kwajalein', b'Pacific/Kwajalein (GMT +1200)'), (b'Pacific/Majuro', b'Pacific/Majuro (GMT +1200)'), (b'Pacific/Marquesas', b'Pacific/Marquesas (GMT -0930)'), (b'Pacific/Midway', b'Pacific/Midway (GMT -1100)'), (b'Pacific/Nauru', b'Pacific/Nauru (GMT +1200)'), (b'Pacific/Niue', b'Pacific/Niue (GMT -1100)'), (b'Pacific/Norfolk', b'Pacific/Norfolk (GMT +1130)'), (b'Pacific/Noumea', b'Pacific/Noumea (GMT +1100)'), (b'Pacific/Pago_Pago', b'Pacific/Pago_Pago (GMT -1100)'), (b'Pacific/Palau', b'Pacific/Palau (GMT +0900)'), (b'Pacific/Pitcairn', b'Pacific/Pitcairn (GMT -0800)'), (b'Pacific/Pohnpei', b'Pacific/Pohnpei (GMT +1100)'), (b'Pacific/Port_Moresby', b'Pacific/Port_Moresby (GMT +1000)'), (b'Pacific/Rarotonga', b'Pacific/Rarotonga (GMT -1000)'), (b'Pacific/Saipan', b'Pacific/Saipan (GMT +1000)'), (b'Pacific/Tahiti', b'Pacific/Tahiti (GMT -1000)'), (b'Pacific/Tarawa', b'Pacific/Tarawa (GMT +1200)'), (b'Pacific/Tongatapu', b'Pacific/Tongatapu (GMT +1300)'), (b'Pacific/Wake', b'Pacific/Wake (GMT +1200)'), (b'Pacific/Wallis', b'Pacific/Wallis (GMT +1200)'), (b'US/Alaska', b'US/Alaska (GMT -0800)'), (b'US/Arizona', b'US/Arizona (GMT -0700)'), (b'US/Central', b'US/Central (GMT -0500)'), (b'US/Eastern', b'US/Eastern (GMT -0400)'), (b'US/Hawaii', b'US/Hawaii (GMT -1000)'), (b'US/Mountain', b'US/Mountain (GMT -0600)'), (b'US/Pacific', b'US/Pacific (GMT -0700)'), (b'UTC', b'UTC (GMT +0000)')], default=b'America/Puerto_Rico', max_length=255)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('skype', models.CharField(blank=True, max_length=50)),
                ('google', models.CharField(blank=True, max_length=50)),
                ('jitsi', models.CharField(blank=True, max_length=50)),
                ('address', models.TextField(blank=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
