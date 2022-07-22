import csv
import io

from django.core.management import BaseCommand

from wsv.models import WorkMetadata, Contributor


class Command(BaseCommand):
    help = "sync_metadata"

    def handle(self, *args, **options):

        with io.open('works_metadata.csv','r') as file:
            reader = csv.reader(file)
            for row in reader:
                contributors = row[1].split('|')
                if not WorkMetadata.objects.filter(iswc=row[2]).exists():

                    if not Contributor.objects.filter(name__in=contributors,metadata__title=row[0]).exists():
                        mtdata = WorkMetadata()
                        mtdata.title = row[0]
                        mtdata.iswc = row[2]
                        mtdata.save()

                        for cont in contributors:
                            dbcont = Contributor()
                            dbcont.name = cont
                            dbcont.metadata = mtdata
                            dbcont.save()
                    else:
                        wm = WorkMetadata.objects.filter(title=row[0])[0]
                        wm.iswc = row[2]
                        wm.save()
                else:
                    for cont in contributors:
                        if not Contributor.objects.filter(name=cont, metadata__iswc=row[2]).exists():
                            dbcont = Contributor()
                            dbcont.name = cont
                            dbcont.metadata = mtdata
                            dbcont.save()
        print("Finished loading metadata")






