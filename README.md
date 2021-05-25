# Anonymise Dicom


Currently, the code is fairly crude. First, it calls the `pydicom` method:

```
    remove_private_tags()
```

and then clears this list of keys in the file:


```
    keys_to_wipe = ['StudyDate', 'SeriesDate', 'AcquisitionDate', 'ContentDate', 'StudyTime',
     'SeriesTime','AcquisitionTime', 'ContentTime', 'AccessionNumber', 'InstitutionName',
     'ReferringPhysicianName', 'StationName', 'PhysiciansOfRecord', 'AdmittingDiagnosesDescription',
     'PatientName', 'PatientID', 'PatientBirthDate', 'PatientSex', 'OtherPatientNames', 'PatientAge',
     'PatientAddress', 'AdditionalPatientHistory', 'PregnancyStatus', 'RequestingPhysician']
```

You can modify this list of keys to suit your own needs.

The code works by taking a source directory which contains some dicom files and it puts the anonymised files in a target directory:

```
usage: dicom_anonymise.py --source sourcedir --dest anonymiseddir

Anonymise folders of DICOM files

optional arguments:
  -h, --help       show this help message and exit
  --source source  source directory
  --dest dest      destination directory
```

## Installation

```
python setup.py install
```

## TODO

There are many possible improvements.

The fields in the dicom file have different possible types and there are many possible ways of anonymising them- for example, you could just clear them, or zero them, delete them, replace with default values etc.

Check out more details on the Dicom fields here:

[Application Level Confidentiality Profile Attributes](http://dicom.nema.org/dicom/2013/output/chtml/part15/chapter_E.html#table_E.1-1)

Appreciate any feedback or pull requests.