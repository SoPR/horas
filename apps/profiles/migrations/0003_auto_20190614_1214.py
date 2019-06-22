# Generated by Django 1.10.7 on 2019-06-14 12:14
# Modified by Raúl Negrón on 2019-06-22 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("profiles", "0002_auto_20170526_0057")]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="timezone",
            field=models.CharField(
                choices=[
                    ("", "--- Selecciona ---"),
                    ("Africa/Abidjan", "Africa/Abidjan (GMT +0000)"),
                    ("Africa/Accra", "Africa/Accra (GMT +0000)"),
                    ("Africa/Addis_Ababa", "Africa/Addis_Ababa (GMT +0300)"),
                    ("Africa/Algiers", "Africa/Algiers (GMT +0100)"),
                    ("Africa/Asmara", "Africa/Asmara (GMT +0300)"),
                    ("Africa/Bamako", "Africa/Bamako (GMT +0000)"),
                    ("Africa/Bangui", "Africa/Bangui (GMT +0100)"),
                    ("Africa/Banjul", "Africa/Banjul (GMT +0000)"),
                    ("Africa/Bissau", "Africa/Bissau (GMT +0000)"),
                    ("Africa/Blantyre", "Africa/Blantyre (GMT +0200)"),
                    ("Africa/Brazzaville", "Africa/Brazzaville (GMT +0100)"),
                    ("Africa/Bujumbura", "Africa/Bujumbura (GMT +0200)"),
                    ("Africa/Cairo", "Africa/Cairo (GMT +0200)"),
                    ("Africa/Casablanca", "Africa/Casablanca (GMT +0100)"),
                    ("Africa/Ceuta", "Africa/Ceuta (GMT +0200)"),
                    ("Africa/Conakry", "Africa/Conakry (GMT +0000)"),
                    ("Africa/Dakar", "Africa/Dakar (GMT +0000)"),
                    ("Africa/Dar_es_Salaam", "Africa/Dar_es_Salaam (GMT +0300)"),
                    ("Africa/Djibouti", "Africa/Djibouti (GMT +0300)"),
                    ("Africa/Douala", "Africa/Douala (GMT +0100)"),
                    ("Africa/El_Aaiun", "Africa/El_Aaiun (GMT +0100)"),
                    ("Africa/Freetown", "Africa/Freetown (GMT +0000)"),
                    ("Africa/Gaborone", "Africa/Gaborone (GMT +0200)"),
                    ("Africa/Harare", "Africa/Harare (GMT +0200)"),
                    ("Africa/Johannesburg", "Africa/Johannesburg (GMT +0200)"),
                    ("Africa/Juba", "Africa/Juba (GMT +0300)"),
                    ("Africa/Kampala", "Africa/Kampala (GMT +0300)"),
                    ("Africa/Khartoum", "Africa/Khartoum (GMT +0300)"),
                    ("Africa/Kigali", "Africa/Kigali (GMT +0200)"),
                    ("Africa/Kinshasa", "Africa/Kinshasa (GMT +0100)"),
                    ("Africa/Lagos", "Africa/Lagos (GMT +0100)"),
                    ("Africa/Libreville", "Africa/Libreville (GMT +0100)"),
                    ("Africa/Lome", "Africa/Lome (GMT +0000)"),
                    ("Africa/Luanda", "Africa/Luanda (GMT +0100)"),
                    ("Africa/Lubumbashi", "Africa/Lubumbashi (GMT +0200)"),
                    ("Africa/Lusaka", "Africa/Lusaka (GMT +0200)"),
                    ("Africa/Malabo", "Africa/Malabo (GMT +0100)"),
                    ("Africa/Maputo", "Africa/Maputo (GMT +0200)"),
                    ("Africa/Maseru", "Africa/Maseru (GMT +0200)"),
                    ("Africa/Mbabane", "Africa/Mbabane (GMT +0200)"),
                    ("Africa/Mogadishu", "Africa/Mogadishu (GMT +0300)"),
                    ("Africa/Monrovia", "Africa/Monrovia (GMT +0000)"),
                    ("Africa/Nairobi", "Africa/Nairobi (GMT +0300)"),
                    ("Africa/Ndjamena", "Africa/Ndjamena (GMT +0100)"),
                    ("Africa/Niamey", "Africa/Niamey (GMT +0100)"),
                    ("Africa/Nouakchott", "Africa/Nouakchott (GMT +0000)"),
                    ("Africa/Ouagadougou", "Africa/Ouagadougou (GMT +0000)"),
                    ("Africa/Porto-Novo", "Africa/Porto-Novo (GMT +0100)"),
                    ("Africa/Sao_Tome", "Africa/Sao_Tome (GMT +0000)"),
                    ("Africa/Tripoli", "Africa/Tripoli (GMT +0200)"),
                    ("Africa/Tunis", "Africa/Tunis (GMT +0100)"),
                    ("Africa/Windhoek", "Africa/Windhoek (GMT +0100)"),
                    ("America/Adak", "America/Adak (GMT -0900)"),
                    ("America/Anchorage", "America/Anchorage (GMT -0800)"),
                    ("America/Anguilla", "America/Anguilla (GMT -0400)"),
                    ("America/Antigua", "America/Antigua (GMT -0400)"),
                    ("America/Araguaina", "America/Araguaina (GMT -0300)"),
                    (
                        "America/Argentina/Buenos_Aires",
                        "America/Argentina/Buenos_Aires (GMT -0300)",
                    ),
                    (
                        "America/Argentina/Catamarca",
                        "America/Argentina/Catamarca (GMT -0300)",
                    ),
                    (
                        "America/Argentina/Cordoba",
                        "America/Argentina/Cordoba (GMT -0300)",
                    ),
                    ("America/Argentina/Jujuy", "America/Argentina/Jujuy (GMT -0300)"),
                    (
                        "America/Argentina/La_Rioja",
                        "America/Argentina/La_Rioja (GMT -0300)",
                    ),
                    (
                        "America/Argentina/Mendoza",
                        "America/Argentina/Mendoza (GMT -0300)",
                    ),
                    (
                        "America/Argentina/Rio_Gallegos",
                        "America/Argentina/Rio_Gallegos (GMT -0300)",
                    ),
                    ("America/Argentina/Salta", "America/Argentina/Salta (GMT -0300)"),
                    (
                        "America/Argentina/San_Juan",
                        "America/Argentina/San_Juan (GMT -0300)",
                    ),
                    (
                        "America/Argentina/San_Luis",
                        "America/Argentina/San_Luis (GMT -0300)",
                    ),
                    (
                        "America/Argentina/Tucuman",
                        "America/Argentina/Tucuman (GMT -0300)",
                    ),
                    (
                        "America/Argentina/Ushuaia",
                        "America/Argentina/Ushuaia (GMT -0300)",
                    ),
                    ("America/Aruba", "America/Aruba (GMT -0400)"),
                    ("America/Asuncion", "America/Asuncion (GMT -0400)"),
                    ("America/Atikokan", "America/Atikokan (GMT -0500)"),
                    ("America/Bahia", "America/Bahia (GMT -0300)"),
                    ("America/Bahia_Banderas", "America/Bahia_Banderas (GMT -0500)"),
                    ("America/Barbados", "America/Barbados (GMT -0400)"),
                    ("America/Belem", "America/Belem (GMT -0300)"),
                    ("America/Belize", "America/Belize (GMT -0600)"),
                    ("America/Blanc-Sablon", "America/Blanc-Sablon (GMT -0400)"),
                    ("America/Boa_Vista", "America/Boa_Vista (GMT -0400)"),
                    ("America/Bogota", "America/Bogota (GMT -0500)"),
                    ("America/Boise", "America/Boise (GMT -0600)"),
                    ("America/Cambridge_Bay", "America/Cambridge_Bay (GMT -0600)"),
                    ("America/Campo_Grande", "America/Campo_Grande (GMT -0400)"),
                    ("America/Cancun", "America/Cancun (GMT -0500)"),
                    ("America/Caracas", "America/Caracas (GMT -0430)"),
                    ("America/Cayenne", "America/Cayenne (GMT -0300)"),
                    ("America/Cayman", "America/Cayman (GMT -0500)"),
                    ("America/Chicago", "America/Chicago (GMT -0500)"),
                    ("America/Chihuahua", "America/Chihuahua (GMT -0600)"),
                    ("America/Costa_Rica", "America/Costa_Rica (GMT -0600)"),
                    ("America/Creston", "America/Creston (GMT -0700)"),
                    ("America/Cuiaba", "America/Cuiaba (GMT -0400)"),
                    ("America/Curacao", "America/Curacao (GMT -0400)"),
                    ("America/Danmarkshavn", "America/Danmarkshavn (GMT +0000)"),
                    ("America/Dawson", "America/Dawson (GMT -0700)"),
                    ("America/Dawson_Creek", "America/Dawson_Creek (GMT -0700)"),
                    ("America/Denver", "America/Denver (GMT -0600)"),
                    ("America/Detroit", "America/Detroit (GMT -0400)"),
                    ("America/Dominica", "America/Dominica (GMT -0400)"),
                    ("America/Edmonton", "America/Edmonton (GMT -0600)"),
                    ("America/Eirunepe", "America/Eirunepe (GMT -0500)"),
                    ("America/El_Salvador", "America/El_Salvador (GMT -0600)"),
                    ("America/Fortaleza", "America/Fortaleza (GMT -0300)"),
                    ("America/Glace_Bay", "America/Glace_Bay (GMT -0300)"),
                    ("America/Godtha", "America/Godthab (GMT -0200)"),
                    ("America/Goose_Bay", "America/Goose_Bay (GMT -0300)"),
                    ("America/Grand_Turk", "America/Grand_Turk (GMT -0400)"),
                    ("America/Grenada", "America/Grenada (GMT -0400)"),
                    ("America/Guadeloupe", "America/Guadeloupe (GMT -0400)"),
                    ("America/Guatemala", "America/Guatemala (GMT -0600)"),
                    ("America/Guayaquil", "America/Guayaquil (GMT -0500)"),
                    ("America/Guyana", "America/Guyana (GMT -0400)"),
                    ("America/Halifax", "America/Halifax (GMT -0300)"),
                    ("America/Havana", "America/Havana (GMT -0400)"),
                    ("America/Hermosillo", "America/Hermosillo (GMT -0700)"),
                    (
                        "America/Indiana/Indianapolis",
                        "America/Indiana/Indianapolis (GMT -0400)",
                    ),
                    ("America/Indiana/Knox", "America/Indiana/Knox (GMT -0500)"),
                    ("America/Indiana/Marengo", "America/Indiana/Marengo (GMT -0400)"),
                    (
                        "America/Indiana/Petersburg",
                        "America/Indiana/Petersburg (GMT -0400)",
                    ),
                    (
                        "America/Indiana/Tell_City",
                        "America/Indiana/Tell_City (GMT -0500)",
                    ),
                    ("America/Indiana/Vevay", "America/Indiana/Vevay (GMT -0400)"),
                    (
                        "America/Indiana/Vincennes",
                        "America/Indiana/Vincennes (GMT -0400)",
                    ),
                    ("America/Indiana/Winamac", "America/Indiana/Winamac (GMT -0400)"),
                    ("America/Inuvik", "America/Inuvik (GMT -0600)"),
                    ("America/Iqaluit", "America/Iqaluit (GMT -0400)"),
                    ("America/Jamaica", "America/Jamaica (GMT -0500)"),
                    ("America/Juneau", "America/Juneau (GMT -0800)"),
                    (
                        "America/Kentucky/Louisville",
                        "America/Kentucky/Louisville (GMT -0400)",
                    ),
                    (
                        "America/Kentucky/Monticello",
                        "America/Kentucky/Monticello (GMT -0400)",
                    ),
                    ("America/Kralendijk", "America/Kralendijk (GMT -0400)"),
                    ("America/La_Paz", "America/La_Paz (GMT -0400)"),
                    ("America/Lima", "America/Lima (GMT -0500)"),
                    ("America/Los_Angeles", "America/Los_Angeles (GMT -0700)"),
                    ("America/Lower_Princes", "America/Lower_Princes (GMT -0400)"),
                    ("America/Maceio", "America/Maceio (GMT -0300)"),
                    ("America/Managua", "America/Managua (GMT -0600)"),
                    ("America/Manaus", "America/Manaus (GMT -0400)"),
                    ("America/Marigot", "America/Marigot (GMT -0400)"),
                    ("America/Martinique", "America/Martinique (GMT -0400)"),
                    ("America/Matamoros", "America/Matamoros (GMT -0500)"),
                    ("America/Mazatlan", "America/Mazatlan (GMT -0600)"),
                    ("America/Menominee", "America/Menominee (GMT -0500)"),
                    ("America/Merida", "America/Merida (GMT -0500)"),
                    ("America/Metlakatla", "America/Metlakatla (GMT -0800)"),
                    ("America/Mexico_City", "America/Mexico_City (GMT -0500)"),
                    ("America/Miquelon", "America/Miquelon (GMT -0200)"),
                    ("America/Moncton", "America/Moncton (GMT -0300)"),
                    ("America/Monterrey", "America/Monterrey (GMT -0500)"),
                    ("America/Montevideo", "America/Montevideo (GMT -0300)"),
                    ("America/Montreal", "America/Montreal (GMT -0400)"),
                    ("America/Montserrat", "America/Montserrat (GMT -0400)"),
                    ("America/Nassau", "America/Nassau (GMT -0400)"),
                    ("America/New_York", "America/New_York (GMT -0400)"),
                    ("America/Nipigon", "America/Nipigon (GMT -0400)"),
                    ("America/Nome", "America/Nome (GMT -0800)"),
                    ("America/Noronha", "America/Noronha (GMT -0200)"),
                    (
                        "America/North_Dakota/Beulah",
                        "America/North_Dakota/Beulah (GMT -0500)",
                    ),
                    (
                        "America/North_Dakota/Center",
                        "America/North_Dakota/Center (GMT -0500)",
                    ),
                    (
                        "America/North_Dakota/New_Salem",
                        "America/North_Dakota/New_Salem (GMT -0500)",
                    ),
                    ("America/Ojinaga", "America/Ojinaga (GMT -0600)"),
                    ("America/Panama", "America/Panama (GMT -0500)"),
                    ("America/Pangnirtung", "America/Pangnirtung (GMT -0400)"),
                    ("America/Paramaribo", "America/Paramaribo (GMT -0300)"),
                    ("America/Phoenix", "America/Phoenix (GMT -0700)"),
                    ("America/Port-au-Prince", "America/Port-au-Prince (GMT -0400)"),
                    ("America/Port_of_Spain", "America/Port_of_Spain (GMT -0400)"),
                    ("America/Porto_Velho", "America/Porto_Velho (GMT -0400)"),
                    ("America/Puerto_Rico", "America/Puerto_Rico (GMT -0400)"),
                    ("America/Rainy_River", "America/Rainy_River (GMT -0500)"),
                    ("America/Rankin_Inlet", "America/Rankin_Inlet (GMT -0500)"),
                    ("America/Recife", "America/Recife (GMT -0300)"),
                    ("America/Regina", "America/Regina (GMT -0600)"),
                    ("America/Resolute", "America/Resolute (GMT -0500)"),
                    ("America/Rio_Branco", "America/Rio_Branco (GMT -0500)"),
                    ("America/Santa_Isabel", "America/Santa_Isabel (GMT -0700)"),
                    ("America/Santarem", "America/Santarem (GMT -0300)"),
                    ("America/Santiago", "America/Santiago (GMT -0400)"),
                    ("America/Santo_Domingo", "America/Santo_Domingo (GMT -0400)"),
                    ("America/Sao_Paulo", "America/Sao_Paulo (GMT -0300)"),
                    ("America/Scoresbysund", "America/Scoresbysund (GMT +0000)"),
                    ("America/Sitka", "America/Sitka (GMT -0800)"),
                    ("America/St_Barthelemy", "America/St_Barthelemy (GMT -0400)"),
                    ("America/St_Johns", "America/St_Johns (GMT -0230)"),
                    ("America/St_Kitts", "America/St_Kitts (GMT -0400)"),
                    ("America/St_Lucia", "America/St_Lucia (GMT -0400)"),
                    ("America/St_Thomas", "America/St_Thomas (GMT -0400)"),
                    ("America/St_Vincent", "America/St_Vincent (GMT -0400)"),
                    ("America/Swift_Current", "America/Swift_Current (GMT -0600)"),
                    ("America/Tegucigalpa", "America/Tegucigalpa (GMT -0600)"),
                    ("America/Thule", "America/Thule (GMT -0300)"),
                    ("America/Thunder_Bay", "America/Thunder_Bay (GMT -0400)"),
                    ("America/Tijuana", "America/Tijuana (GMT -0700)"),
                    ("America/Toronto", "America/Toronto (GMT -0400)"),
                    ("America/Tortola", "America/Tortola (GMT -0400)"),
                    ("America/Vancouver", "America/Vancouver (GMT -0700)"),
                    ("America/Whitehorse", "America/Whitehorse (GMT -0700)"),
                    ("America/Winnipeg", "America/Winnipeg (GMT -0500)"),
                    ("America/Yakutat", "America/Yakutat (GMT -0800)"),
                    ("America/Yellowknife", "America/Yellowknife (GMT -0600)"),
                    ("Antarctica/Casey", "Antarctica/Casey (GMT +0800)"),
                    ("Antarctica/Davis", "Antarctica/Davis (GMT +0700)"),
                    (
                        "Antarctica/DumontDUrville",
                        "Antarctica/DumontDUrville (GMT +1000)",
                    ),
                    ("Antarctica/Macquarie", "Antarctica/Macquarie (GMT +1100)"),
                    ("Antarctica/Mawson", "Antarctica/Mawson (GMT +0500)"),
                    ("Antarctica/McMurdo", "Antarctica/McMurdo (GMT +1200)"),
                    ("Antarctica/Palmer", "Antarctica/Palmer (GMT -0400)"),
                    ("Antarctica/Rothera", "Antarctica/Rothera (GMT -0300)"),
                    ("Antarctica/Syowa", "Antarctica/Syowa (GMT +0300)"),
                    ("Antarctica/Troll", "Antarctica/Troll (GMT +0200)"),
                    ("Antarctica/Vostok", "Antarctica/Vostok (GMT +0600)"),
                    ("Arctic/Longyearbyen", "Arctic/Longyearbyen (GMT +0200)"),
                    ("Asia/Aden", "Asia/Aden (GMT +0300)"),
                    ("Asia/Almaty", "Asia/Almaty (GMT +0600)"),
                    ("Asia/Amman", "Asia/Amman (GMT +0300)"),
                    ("Asia/Anadyr", "Asia/Anadyr (GMT +1200)"),
                    ("Asia/Aqtau", "Asia/Aqtau (GMT +0500)"),
                    ("Asia/Aqtobe", "Asia/Aqtobe (GMT +0500)"),
                    ("Asia/Ashgabat", "Asia/Ashgabat (GMT +0500)"),
                    ("Asia/Baghdad", "Asia/Baghdad (GMT +0300)"),
                    ("Asia/Bahrain", "Asia/Bahrain (GMT +0300)"),
                    ("Asia/Baku", "Asia/Baku (GMT +0500)"),
                    ("Asia/Bangkok", "Asia/Bangkok (GMT +0700)"),
                    ("Asia/Beirut", "Asia/Beirut (GMT +0300)"),
                    ("Asia/Bishkek", "Asia/Bishkek (GMT +0600)"),
                    ("Asia/Brunei", "Asia/Brunei (GMT +0800)"),
                    ("Asia/Choibalsan", "Asia/Choibalsan (GMT +0800)"),
                    ("Asia/Chongqing", "Asia/Chongqing (GMT +0800)"),
                    ("Asia/Colombo", "Asia/Colombo (GMT +0530)"),
                    ("Asia/Damascus", "Asia/Damascus (GMT +0300)"),
                    ("Asia/Dhaka", "Asia/Dhaka (GMT +0600)"),
                    ("Asia/Dili", "Asia/Dili (GMT +0900)"),
                    ("Asia/Dubai", "Asia/Dubai (GMT +0400)"),
                    ("Asia/Dushanbe", "Asia/Dushanbe (GMT +0500)"),
                    ("Asia/Gaza", "Asia/Gaza (GMT +0300)"),
                    ("Asia/Harbin", "Asia/Harbin (GMT +0800)"),
                    ("Asia/Hebron", "Asia/Hebron (GMT +0300)"),
                    ("Asia/Ho_Chi_Minh", "Asia/Ho_Chi_Minh (GMT +0700)"),
                    ("Asia/Hong_Kong", "Asia/Hong_Kong (GMT +0800)"),
                    ("Asia/Hovd", "Asia/Hovd (GMT +0700)"),
                    ("Asia/Irkutsk", "Asia/Irkutsk (GMT +0900)"),
                    ("Asia/Jakarta", "Asia/Jakarta (GMT +0700)"),
                    ("Asia/Jayapura", "Asia/Jayapura (GMT +0900)"),
                    ("Asia/Jerusalem", "Asia/Jerusalem (GMT +0300)"),
                    ("Asia/Kabul", "Asia/Kabul (GMT +0430)"),
                    ("Asia/Kamchatka", "Asia/Kamchatka (GMT +1200)"),
                    ("Asia/Karachi", "Asia/Karachi (GMT +0500)"),
                    ("Asia/Kashgar", "Asia/Kashgar (GMT +0800)"),
                    ("Asia/Kathmandu", "Asia/Kathmandu (GMT +0545)"),
                    ("Asia/Khandyga", "Asia/Khandyga (GMT +1000)"),
                    ("Asia/Kolkata", "Asia/Kolkata (GMT +0530)"),
                    ("Asia/Krasnoyarsk", "Asia/Krasnoyarsk (GMT +0800)"),
                    ("Asia/Kuala_Lumpur", "Asia/Kuala_Lumpur (GMT +0800)"),
                    ("Asia/Kuching", "Asia/Kuching (GMT +0800)"),
                    ("Asia/Kuwait", "Asia/Kuwait (GMT +0300)"),
                    ("Asia/Macau", "Asia/Macau (GMT +0800)"),
                    ("Asia/Magadan", "Asia/Magadan (GMT +1200)"),
                    ("Asia/Makassar", "Asia/Makassar (GMT +0800)"),
                    ("Asia/Manila", "Asia/Manila (GMT +0800)"),
                    ("Asia/Muscat", "Asia/Muscat (GMT +0400)"),
                    ("Asia/Nicosia", "Asia/Nicosia (GMT +0300)"),
                    ("Asia/Novokuznetsk", "Asia/Novokuznetsk (GMT +0700)"),
                    ("Asia/Novosibirsk", "Asia/Novosibirsk (GMT +0700)"),
                    ("Asia/Omsk", "Asia/Omsk (GMT +0700)"),
                    ("Asia/Oral", "Asia/Oral (GMT +0500)"),
                    ("Asia/Phnom_Penh", "Asia/Phnom_Penh (GMT +0700)"),
                    ("Asia/Pontianak", "Asia/Pontianak (GMT +0700)"),
                    ("Asia/Pyongyang", "Asia/Pyongyang (GMT +0900)"),
                    ("Asia/Qatar", "Asia/Qatar (GMT +0300)"),
                    ("Asia/Qyzylorda", "Asia/Qyzylorda (GMT +0600)"),
                    ("Asia/Rangoon", "Asia/Rangoon (GMT +0630)"),
                    ("Asia/Riyadh", "Asia/Riyadh (GMT +0300)"),
                    ("Asia/Sakhalin", "Asia/Sakhalin (GMT +1100)"),
                    ("Asia/Samarkand", "Asia/Samarkand (GMT +0500)"),
                    ("Asia/Seoul", "Asia/Seoul (GMT +0900)"),
                    ("Asia/Shanghai", "Asia/Shanghai (GMT +0800)"),
                    ("Asia/Singapore", "Asia/Singapore (GMT +0800)"),
                    ("Asia/Taipei", "Asia/Taipei (GMT +0800)"),
                    ("Asia/Tashkent", "Asia/Tashkent (GMT +0500)"),
                    ("Asia/Tbilisi", "Asia/Tbilisi (GMT +0400)"),
                    ("Asia/Tehran", "Asia/Tehran (GMT +0430)"),
                    ("Asia/Thimphu", "Asia/Thimphu (GMT +0600)"),
                    ("Asia/Tokyo", "Asia/Tokyo (GMT +0900)"),
                    ("Asia/Ulaanbaatar", "Asia/Ulaanbaatar (GMT +0800)"),
                    ("Asia/Urumqi", "Asia/Urumqi (GMT +0800)"),
                    ("Asia/Ust-Nera", "Asia/Ust-Nera (GMT +1100)"),
                    ("Asia/Vientiane", "Asia/Vientiane (GMT +0700)"),
                    ("Asia/Vladivostok", "Asia/Vladivostok (GMT +1100)"),
                    ("Asia/Yakutsk", "Asia/Yakutsk (GMT +1000)"),
                    ("Asia/Yekaterinburg", "Asia/Yekaterinburg (GMT +0600)"),
                    ("Asia/Yerevan", "Asia/Yerevan (GMT +0400)"),
                    ("Atlantic/Azores", "Atlantic/Azores (GMT +0000)"),
                    ("Atlantic/Bermuda", "Atlantic/Bermuda (GMT -0300)"),
                    ("Atlantic/Canary", "Atlantic/Canary (GMT +0100)"),
                    ("Atlantic/Cape_Verde", "Atlantic/Cape_Verde (GMT -0100)"),
                    ("Atlantic/Faroe", "Atlantic/Faroe (GMT +0100)"),
                    ("Atlantic/Madeira", "Atlantic/Madeira (GMT +0100)"),
                    ("Atlantic/Reykjavik", "Atlantic/Reykjavik (GMT +0000)"),
                    ("Atlantic/South_Georgia", "Atlantic/South_Georgia (GMT -0200)"),
                    ("Atlantic/St_Helena", "Atlantic/St_Helena (GMT +0000)"),
                    ("Atlantic/Stanley", "Atlantic/Stanley (GMT -0300)"),
                    ("Australia/Adelaide", "Australia/Adelaide (GMT +0930)"),
                    ("Australia/Brisbane", "Australia/Brisbane (GMT +1000)"),
                    ("Australia/Broken_Hill", "Australia/Broken_Hill (GMT +0930)"),
                    ("Australia/Currie", "Australia/Currie (GMT +1000)"),
                    ("Australia/Darwin", "Australia/Darwin (GMT +0930)"),
                    ("Australia/Eucla", "Australia/Eucla (GMT +0845)"),
                    ("Australia/Hobart", "Australia/Hobart (GMT +1000)"),
                    ("Australia/Lindeman", "Australia/Lindeman (GMT +1000)"),
                    ("Australia/Lord_Howe", "Australia/Lord_Howe (GMT +1030)"),
                    ("Australia/Melbourne", "Australia/Melbourne (GMT +1000)"),
                    ("Australia/Perth", "Australia/Perth (GMT +0800)"),
                    ("Australia/Sydney", "Australia/Sydney (GMT +1000)"),
                    ("Canada/Atlantic", "Canada/Atlantic (GMT -0300)"),
                    ("Canada/Central", "Canada/Central (GMT -0500)"),
                    ("Canada/Eastern", "Canada/Eastern (GMT -0400)"),
                    ("Canada/Mountain", "Canada/Mountain (GMT -0600)"),
                    ("Canada/Newfoundland", "Canada/Newfoundland (GMT -0230)"),
                    ("Canada/Pacific", "Canada/Pacific (GMT -0700)"),
                    ("Europe/Amsterdam", "Europe/Amsterdam (GMT +0200)"),
                    ("Europe/Andorra", "Europe/Andorra (GMT +0200)"),
                    ("Europe/Athens", "Europe/Athens (GMT +0300)"),
                    ("Europe/Belgrade", "Europe/Belgrade (GMT +0200)"),
                    ("Europe/Berlin", "Europe/Berlin (GMT +0200)"),
                    ("Europe/Bratislava", "Europe/Bratislava (GMT +0200)"),
                    ("Europe/Brussels", "Europe/Brussels (GMT +0200)"),
                    ("Europe/Bucharest", "Europe/Bucharest (GMT +0300)"),
                    ("Europe/Budapest", "Europe/Budapest (GMT +0200)"),
                    ("Europe/Busingen", "Europe/Busingen (GMT +0200)"),
                    ("Europe/Chisinau", "Europe/Chisinau (GMT +0300)"),
                    ("Europe/Copenhagen", "Europe/Copenhagen (GMT +0200)"),
                    ("Europe/Dublin", "Europe/Dublin (GMT +0100)"),
                    ("Europe/Gibraltar", "Europe/Gibraltar (GMT +0200)"),
                    ("Europe/Guernsey", "Europe/Guernsey (GMT +0100)"),
                    ("Europe/Helsinki", "Europe/Helsinki (GMT +0300)"),
                    ("Europe/Isle_of_Man", "Europe/Isle_of_Man (GMT +0100)"),
                    ("Europe/Istanbul", "Europe/Istanbul (GMT +0300)"),
                    ("Europe/Jersey", "Europe/Jersey (GMT +0100)"),
                    ("Europe/Kaliningrad", "Europe/Kaliningrad (GMT +0300)"),
                    ("Europe/Kiev", "Europe/Kiev (GMT +0300)"),
                    ("Europe/Lisbon", "Europe/Lisbon (GMT +0100)"),
                    ("Europe/Ljubljana", "Europe/Ljubljana (GMT +0200)"),
                    ("Europe/London", "Europe/London (GMT +0100)"),
                    ("Europe/Luxembourg", "Europe/Luxembourg (GMT +0200)"),
                    ("Europe/Madrid", "Europe/Madrid (GMT +0200)"),
                    ("Europe/Malta", "Europe/Malta (GMT +0200)"),
                    ("Europe/Mariehamn", "Europe/Mariehamn (GMT +0300)"),
                    ("Europe/Minsk", "Europe/Minsk (GMT +0300)"),
                    ("Europe/Monaco", "Europe/Monaco (GMT +0200)"),
                    ("Europe/Moscow", "Europe/Moscow (GMT +0400)"),
                    ("Europe/Oslo", "Europe/Oslo (GMT +0200)"),
                    ("Europe/Paris", "Europe/Paris (GMT +0200)"),
                    ("Europe/Podgorica", "Europe/Podgorica (GMT +0200)"),
                    ("Europe/Prague", "Europe/Prague (GMT +0200)"),
                    ("Europe/Riga", "Europe/Riga (GMT +0300)"),
                    ("Europe/Rome", "Europe/Rome (GMT +0200)"),
                    ("Europe/Samara", "Europe/Samara (GMT +0400)"),
                    ("Europe/San_Marino", "Europe/San_Marino (GMT +0200)"),
                    ("Europe/Sarajevo", "Europe/Sarajevo (GMT +0200)"),
                    ("Europe/Simferopol", "Europe/Simferopol (GMT +0400)"),
                    ("Europe/Skopje", "Europe/Skopje (GMT +0200)"),
                    ("Europe/Sofia", "Europe/Sofia (GMT +0300)"),
                    ("Europe/Stockholm", "Europe/Stockholm (GMT +0200)"),
                    ("Europe/Tallinn", "Europe/Tallinn (GMT +0300)"),
                    ("Europe/Tirane", "Europe/Tirane (GMT +0200)"),
                    ("Europe/Uzhgorod", "Europe/Uzhgorod (GMT +0300)"),
                    ("Europe/Vaduz", "Europe/Vaduz (GMT +0200)"),
                    ("Europe/Vatican", "Europe/Vatican (GMT +0200)"),
                    ("Europe/Vienna", "Europe/Vienna (GMT +0200)"),
                    ("Europe/Vilnius", "Europe/Vilnius (GMT +0300)"),
                    ("Europe/Volgograd", "Europe/Volgograd (GMT +0400)"),
                    ("Europe/Warsaw", "Europe/Warsaw (GMT +0200)"),
                    ("Europe/Zagre", "Europe/Zagreb (GMT +0200)"),
                    ("Europe/Zaporozhye", "Europe/Zaporozhye (GMT +0300)"),
                    ("Europe/Zurich", "Europe/Zurich (GMT +0200)"),
                    ("GMT", "GMT (GMT +0000)"),
                    ("Indian/Antananarivo", "Indian/Antananarivo (GMT +0300)"),
                    ("Indian/Chagos", "Indian/Chagos (GMT +0600)"),
                    ("Indian/Christmas", "Indian/Christmas (GMT +0700)"),
                    ("Indian/Cocos", "Indian/Cocos (GMT +0630)"),
                    ("Indian/Comoro", "Indian/Comoro (GMT +0300)"),
                    ("Indian/Kerguelen", "Indian/Kerguelen (GMT +0500)"),
                    ("Indian/Mahe", "Indian/Mahe (GMT +0400)"),
                    ("Indian/Maldives", "Indian/Maldives (GMT +0500)"),
                    ("Indian/Mauritius", "Indian/Mauritius (GMT +0400)"),
                    ("Indian/Mayotte", "Indian/Mayotte (GMT +0300)"),
                    ("Indian/Reunion", "Indian/Reunion (GMT +0400)"),
                    ("Pacific/Apia", "Pacific/Apia (GMT +1300)"),
                    ("Pacific/Auckland", "Pacific/Auckland (GMT +1200)"),
                    ("Pacific/Chatham", "Pacific/Chatham (GMT +1245)"),
                    ("Pacific/Chuuk", "Pacific/Chuuk (GMT +1000)"),
                    ("Pacific/Easter", "Pacific/Easter (GMT -0600)"),
                    ("Pacific/Efate", "Pacific/Efate (GMT +1100)"),
                    ("Pacific/Enderbury", "Pacific/Enderbury (GMT +1300)"),
                    ("Pacific/Fakaofo", "Pacific/Fakaofo (GMT +1300)"),
                    ("Pacific/Fiji", "Pacific/Fiji (GMT +1200)"),
                    ("Pacific/Funafuti", "Pacific/Funafuti (GMT +1200)"),
                    ("Pacific/Galapagos", "Pacific/Galapagos (GMT -0600)"),
                    ("Pacific/Gambier", "Pacific/Gambier (GMT -0900)"),
                    ("Pacific/Guadalcanal", "Pacific/Guadalcanal (GMT +1100)"),
                    ("Pacific/Guam", "Pacific/Guam (GMT +1000)"),
                    ("Pacific/Honolulu", "Pacific/Honolulu (GMT -1000)"),
                    ("Pacific/Johnston", "Pacific/Johnston (GMT -1000)"),
                    ("Pacific/Kiritimati", "Pacific/Kiritimati (GMT +1400)"),
                    ("Pacific/Kosrae", "Pacific/Kosrae (GMT +1100)"),
                    ("Pacific/Kwajalein", "Pacific/Kwajalein (GMT +1200)"),
                    ("Pacific/Majuro", "Pacific/Majuro (GMT +1200)"),
                    ("Pacific/Marquesas", "Pacific/Marquesas (GMT -0930)"),
                    ("Pacific/Midway", "Pacific/Midway (GMT -1100)"),
                    ("Pacific/Nauru", "Pacific/Nauru (GMT +1200)"),
                    ("Pacific/Niue", "Pacific/Niue (GMT -1100)"),
                    ("Pacific/Norfolk", "Pacific/Norfolk (GMT +1130)"),
                    ("Pacific/Noumea", "Pacific/Noumea (GMT +1100)"),
                    ("Pacific/Pago_Pago", "Pacific/Pago_Pago (GMT -1100)"),
                    ("Pacific/Palau", "Pacific/Palau (GMT +0900)"),
                    ("Pacific/Pitcairn", "Pacific/Pitcairn (GMT -0800)"),
                    ("Pacific/Pohnpei", "Pacific/Pohnpei (GMT +1100)"),
                    ("Pacific/Port_Moresby", "Pacific/Port_Moresby (GMT +1000)"),
                    ("Pacific/Rarotonga", "Pacific/Rarotonga (GMT -1000)"),
                    ("Pacific/Saipan", "Pacific/Saipan (GMT +1000)"),
                    ("Pacific/Tahiti", "Pacific/Tahiti (GMT -1000)"),
                    ("Pacific/Tarawa", "Pacific/Tarawa (GMT +1200)"),
                    ("Pacific/Tongatapu", "Pacific/Tongatapu (GMT +1300)"),
                    ("Pacific/Wake", "Pacific/Wake (GMT +1200)"),
                    ("Pacific/Wallis", "Pacific/Wallis (GMT +1200)"),
                    ("US/Alaska", "US/Alaska (GMT -0800)"),
                    ("US/Arizona", "US/Arizona (GMT -0700)"),
                    ("US/Central", "US/Central (GMT -0500)"),
                    ("US/Eastern", "US/Eastern (GMT -0400)"),
                    ("US/Hawaii", "US/Hawaii (GMT -1000)"),
                    ("US/Mountain", "US/Mountain (GMT -0600)"),
                    ("US/Pacific", "US/Pacific (GMT -0700)"),
                    ("UTC", "UTC (GMT +0000)"),
                ],
                default="America/Puerto_Rico",
                max_length=255,
            ),
        )
    ]
