def transform_scalars(dataset, background_value=0):
    """Converts a label map of connected components of foreground-valued
    voxels in the input image to a label map where each connected component
    has a unique label. Foreground voxels have any value other than the
    background value. Input images are expected to have integral voxel types,
    i.e., no float or double voxels. The connected component labels are ordered
    such that the smallest connected components have the lowest label values and
    the largest connected components have the highest label values.
    """

    from tomviz import utils
    utils.connected_components(dataset, background_value)
