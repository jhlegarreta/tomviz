# Shift a 3D dataset using SciPy Interpolation libraries.
#
# Developed as part of the tomviz project (www.tomviz.com).


def transform_scalars(dataset, SHIFT=None):

    from tomviz import utils
    from scipy import ndimage

    data_py = utils.get_array(dataset) # Get data as numpy array.

    if data_py is None: #Check if data exists
        raise RuntimeError("No data array found!")

    print('Shifting Images...')

    data_py_return = ndimage.interpolation.shift(data_py, SHIFT, order=0)

    utils.set_array(dataset, data_py_return)
    print('Shifting Complete')
