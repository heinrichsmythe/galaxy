# NOTE(cutwater): This migration is replaced by v2_4_0 and should be
#   deleted once superseding migration is merged into master.
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [('main', '0030_auto_20151127_0824')]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='owner',
            field=models.ForeignKey(
                related_name='repositories',
                to=settings.AUTH_USER_MODEL,
                on_delete=models.CASCADE,
            ),
        ),
        migrations.AlterUniqueTogether(
            name='stargazer',
            unique_together={('owner', 'github_user', 'github_repo')},
        ),
        migrations.AlterUniqueTogether(
            name='subscription',
            unique_together={('owner', 'github_user', 'github_repo')},
        ),
        migrations.AlterIndexTogether(
            name='stargazer', index_together=set()
        ),
        migrations.AlterIndexTogether(
            name='subscription', index_together=set()
        ),
    ]
