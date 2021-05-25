import sys
import argparse
import pydicom
import magic # pip install magic python-magic
from pathlib import Path
import os
import traceback

keys_to_wipe = ['StudyDate', 'SeriesDate', 'AcquisitionDate', 'ContentDate', 'StudyTime',
     'SeriesTime','AcquisitionTime', 'ContentTime', 'AccessionNumber', 'InstitutionName',
     'ReferringPhysicianName', 'StationName', 'PhysiciansOfRecord', 'AdmittingDiagnosesDescription',
     'PatientName', 'PatientID', 'PatientBirthDate', 'PatientSex', 'OtherPatientNames', 'PatientAge',
     'PatientAddress', 'AdditionalPatientHistory', 'PregnancyStatus', 'RequestingPhysician']
    

def anonymise_dicom(filename):
    d = pydicom.dcmread(filename)
    d.remove_private_tags()
    
    for key in keys_to_wipe:
        if key in d:
            try:
                #print('setting', key, value)
                d[key].clear()
            except:
                print('ERROR!', key, traceback.format_exc())
        else:
            #print('key not in dataset')
            pass
    return d

def anonymise(source, dest):
    print(f"Anonymising files from {source} to {dest}")

    source = Path(source)
    dest = Path(dest)

    if source == None or dest == None or os.path.isdir(source) is False or os.path.isdir(dest) is False:
        print("source and dest must be directories")
        
    if source == dest:
        print("dest cannot be the same as source")
        return

    if dest.exists() is False:
        dest.mkdir(exist_ok=True, parents=True)

    if os.listdir(dest):
        print('dest must be empty')    
        return

        
    #if True: return
    for fname in source.glob('**/*'):
        if fname.is_file() and 'DICOM' in magic.from_file(fname.as_posix()):
            output = dest / fname.relative_to(source)
            output.parents[0].mkdir(parents=True, exist_ok=True)
            d = anonymise_dicom(fname.as_posix())
            print(f"# {fname} -> {output}")
            d.save_as(output.as_posix())
    return

def main():
    parser = argparse.ArgumentParser(description='Anonymise folders of DICOM files',
                                     usage="dicom_anonymise.py --source sourcedir --dest anonymiseddir",
                                     add_help=True)
    parser.add_argument('--source', metavar='source', type=str,
                        help='source directory', default=None)
    parser.add_argument('--dest', metavar='dest', type=str,
                        help='destination directory', default=None)
    args = parser.parse_args()
    if len(sys.argv) > 1:
        anonymise(args.source, args.dest)

    return

if __name__ == '__main__':
    main()