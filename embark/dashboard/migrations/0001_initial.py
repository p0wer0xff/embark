# Generated by Django 4.1.1 on 2022-10-06 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('architecture_verified', models.CharField(blank=True, max_length=100, null=True)),
                ('os_verified', models.CharField(blank=True, max_length=256, null=True)),
                ('emba_command', models.CharField(blank=True, max_length=762, null=True)),
                ('files', models.IntegerField(default=0)),
                ('directories', models.IntegerField(default=0)),
                ('entropy_value', models.FloatField(default=0.0)),
                ('certificates', models.IntegerField(default=0)),
                ('certificates_outdated', models.IntegerField(default=0)),
                ('shell_scripts', models.IntegerField(default=0)),
                ('shell_script_vulns', models.IntegerField(default=0)),
                ('yara_rules_match', models.IntegerField(default=0)),
                ('kernel_modules', models.IntegerField(default=0)),
                ('kernel_modules_lic', models.IntegerField(default=0)),
                ('interesting_files', models.IntegerField(default=0)),
                ('post_files', models.IntegerField(default=0)),
                ('canary', models.IntegerField(default=0)),
                ('canary_per', models.IntegerField(default=0)),
                ('relro', models.IntegerField(default=0)),
                ('relro_per', models.IntegerField(default=0)),
                ('no_exec', models.IntegerField(default=0)),
                ('no_exec_per', models.IntegerField(default=0)),
                ('pie', models.IntegerField(default=0)),
                ('pie_per', models.IntegerField(default=0)),
                ('stripped', models.IntegerField(default=0)),
                ('stripped_per', models.IntegerField(default=0)),
                ('strcpy', models.IntegerField(default=0)),
                ('versions_identified', models.IntegerField(default=0)),
                ('cve_high', models.IntegerField(default=0)),
                ('cve_medium', models.IntegerField(default=0)),
                ('cve_low', models.IntegerField(default=0)),
                ('exploits', models.IntegerField(default=0)),
                ('metasploit_modules', models.IntegerField(default=0)),
                ('bins_checked', models.IntegerField(default=0)),
                ('strcpy_bin', models.TextField(default='{}')),
            ],
        ),
    ]
