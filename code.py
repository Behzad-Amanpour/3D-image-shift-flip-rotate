"""
Inputs:
    This code is based on a 3D NIfTI Image
    You can find a DICOM Image at this address: https://drive.google.com/file/d/12biFTm_n0enxjQesIwjQLxMey7MuDwmA/view?usp=sharing
"""

from pydicom import dcmread
import matplotlib.pyplot as plt
import numpy as np

# NIfTI Read ===================================================== Behzad Amanpour ==============================
Im_file = nib.load('address on your drive\brain.nii')

Im_3D = Im_file.get_fdata()

Im_3D = np.int16(Im_3D)

# 2D Flip ======================================================== Behzad Amanpour ==============================
Im2_3D = np.flip(Im_3D,2)

Im_file2 = nib.Nifti1Image(Im2_3D, Im_file.affine, Im_file.header)

nib.save(Im_file2, 'brain_edited.nii')
# 2D Shift (Translation) ========================================= Behzad Amanpour ==============================
Im2_3D = np.roll(Im_3D, 50, axis=1)

Im_file2 = nib.Nifti1Image(Im2_3D, Im_file.affine, Im_file.header)

nib.save(Im_file2, 'brain_edited.nii')

Im2_3D[:,0:49,:]=0

Im_file2 = nib.Nifti1Image(Im2_3D, Im_file.affine, Im_file.header)

nib.save(Im_file2, 'brain_edited.nii')

# 2D Rotation ===================================================== Behzad Amanpour ==============================
from scipy import ndimage

Im2_3D = ndimage.rotate(Im_3D, 45, axes=(0,1), reshape=False)

Im_file2 = nib.Nifti1Image(Im2_3D, Im_file.affine, Im_file.header)

nib.save(Im_file2, 'brain_edited.nii')

Im2_3D = ndimage.rotate(Im_3D, -45, axes=(0,1), reshape=True)


# DICOM Write ====================================================== Behzad Amanpour ==============================
Im_file2 = nib.Nifti1Image(Im2_3D, Im_file.affine, Im_file.header)

nib.save(Im_file2, 'brain_edited.nii')
