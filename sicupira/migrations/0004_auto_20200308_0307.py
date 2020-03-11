# Generated by Django 2.2.10 on 2020-03-08 06:07

from django.db import migrations, models
import django.db.models.constraints
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sicupira', '0003_auto_20200223_1012'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaConcentracao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_area_concentracao', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='AreaConcentracaoxDisciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_concentracao_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AreaAreaConcentracaoxDisciplina', to='sicupira.AreaConcentracao')),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaDocente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_categoria', models.CharField(max_length=45, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_curso', models.CharField(max_length=100, unique=True)),
                ('creditos_titulacao', models.IntegerField(default=0)),
                ('disciplina', models.IntegerField(default=0)),
                ('trabalho_conclusao', models.IntegerField(default=0)),
                ('outros', models.IntegerField(default=0)),
                ('equivalencia_hora', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CursoxDisciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carga_horaria', models.IntegerField(default=0)),
                ('curso_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CursoCursoxDiscipliana', to='sicupira.Curso')),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_disciplina', models.CharField(max_length=100, unique=True)),
                ('sigla', models.CharField(max_length=20, unique=True)),
                ('numero', models.CharField(max_length=450, unique=True)),
                ('creditos', models.IntegerField(default=0)),
                ('ementa', models.TextField(blank=True, null=True)),
                ('bibliografia', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EnderecoPrograma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.IntegerField()),
                ('logradouro', models.CharField(max_length=200)),
                ('numero', models.CharField(max_length=20)),
                ('complemento', models.CharField(blank=True, max_length=300, null=True)),
                ('bairro', models.CharField(max_length=100)),
                ('municipio', models.CharField(max_length=100)),
                ('fax', models.CharField(max_length=20)),
                ('telefone', models.CharField(max_length=20)),
                ('ramal', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('web_site', models.CharField(blank=True, max_length=255, null=True)),
                ('inicio', models.DateField()),
                ('fim', models.DateField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('sigla', models.CharField(max_length=2, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('codigo_cnpq', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='LinhaPesquisa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_linha_pesquisa', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Modalidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_modalidade', models.CharField(max_length=45, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='NivelGraduacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_nivel_graduacao', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_nota', models.CharField(max_length=45, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_pais', models.CharField(max_length=100, unique=True)),
                ('codigo_iso', models.CharField(blank=True, max_length=3, null=True, unique=True)),
                ('ddd', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PeriodoLetivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_periodo_letivo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_programa', models.CharField(max_length=20, unique=True)),
                ('nome_programa', models.CharField(max_length=200, unique=True)),
                ('nome_ingles', models.CharField(max_length=200, unique=True)),
                ('flg_cooperacao', models.IntegerField(default=0)),
                ('flg_rede', models.IntegerField(default=0)),
                ('estado_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='EstadoPrograma', to='sicupira.Estado')),
                ('linha_pesquisa_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='LinhaPesquisaPrograma', to='sicupira.LinhaPesquisa')),
                ('modalidade_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ModlidadePrograma', to='sicupira.Modalidade')),
                ('nota', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='NotaPrograma', to='sicupira.Nota')),
            ],
        ),
        migrations.CreateModel(
            name='Regiao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_regiao', models.CharField(max_length=60, unique=True)),
                ('pais_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='PaisRegiao', to='sicupira.Pais')),
            ],
        ),
        migrations.CreateModel(
            name='RegimeLetivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_regime_letivo', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegimeTrabalho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_regime_trabalho', models.CharField(max_length=45, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_sexo', models.CharField(max_length=45, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Situacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_situacao', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SituacaoMatricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_situacao_matricula', models.CharField(max_length=45, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TelefoneEnderecoPrograma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.IntegerField()),
                ('ddd', models.IntegerField()),
                ('numero', models.CharField(max_length=10)),
                ('ramal', models.CharField(blank=True, max_length=20, null=True)),
                ('endereco_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='EnderecoTelefone', to='sicupira.EnderecoPrograma')),
            ],
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_tipo_doc', models.CharField(max_length=45, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField(default=0)),
                ('curso_id', models.ForeignKey(on_delete=django.db.models.constraints.CheckConstraint, related_name='TurmaCurso', to='sicupira.Curso')),
                ('disciplina_id', models.ForeignKey(on_delete=django.db.models.constraints.CheckConstraint, related_name='TurmaDiscipliana', to='sicupira.Disciplina')),
                ('periodo_letivo_id', models.ForeignKey(on_delete=django.db.models.constraints.CheckConstraint, related_name='TurmaPeriodoLeitivo', to='sicupira.PeriodoLetivo')),
            ],
        ),
        migrations.CreateModel(
            name='VincluloIES',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_vinclulo_ies', models.CharField(max_length=45, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Endereco',
        ),
        migrations.DeleteModel(
            name='UF',
        ),
        migrations.AddField(
            model_name='programa',
            name='regiao_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='RegiaoPrograma', to='sicupira.Regiao'),
        ),
        migrations.AddField(
            model_name='programa',
            name='regime_letivo_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='RegimeLetivoPrograma', to='sicupira.RegimeLetivo'),
        ),
        migrations.AddField(
            model_name='programa',
            name='situacao_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='SituacaoPrograma', to='sicupira.Situacao'),
        ),
        migrations.AddField(
            model_name='periodoletivo',
            name='regime_letivo_id',
            field=models.ForeignKey(on_delete=django.db.models.constraints.CheckConstraint, related_name='RegimePeriodoLetivo', to='sicupira.RegimeLetivo'),
        ),
        migrations.AddField(
            model_name='estado',
            name='pais_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='PaisEstado', to='sicupira.Pais'),
        ),
        migrations.AddField(
            model_name='enderecoprograma',
            name='estado_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sicupira.Estado'),
        ),
        migrations.AddField(
            model_name='enderecoprograma',
            name='programa_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProgramaEndereco', to='sicupira.Programa'),
        ),
        migrations.AddField(
            model_name='cursoxdisciplina',
            name='disciplina_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DisciplinaCursoxDiscipliana', to='sicupira.Disciplina'),
        ),
        migrations.AddField(
            model_name='curso',
            name='nivel_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='NivelCurso', to='sicupira.NivelGraduacao'),
        ),
        migrations.AddField(
            model_name='curso',
            name='programa_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ProgramaCurso', to='sicupira.Programa'),
        ),
        migrations.AddField(
            model_name='curso',
            name='situacao_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='SituacaoCurso', to='sicupira.Situacao'),
        ),
        migrations.AddField(
            model_name='areaconcentracaoxdisciplina',
            name='disciplina_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DisciplinaAreaConcentracaoxDisciplina', to='sicupira.Disciplina'),
        ),
        migrations.AddField(
            model_name='areaconcentracao',
            name='programa_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Programa', to='sicupira.Programa'),
        ),
    ]