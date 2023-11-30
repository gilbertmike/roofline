import matplotlib.pyplot as plt

M = 1000  # a large number to make long horizontal line

def compute_inflection_point(compute_throughput, memory_bandwidth):
    """Compute operational intensity of the roofline inflection point"""
    return compute_throughput/memory_bandwidth

def draw_roofline(compute_throughput, memory_bandwidth, **kwargs):
    if 'ax' in kwargs:
        ax = kwargs['ax']
        del kwargs['ax']
    else:
        _, ax = plt.subplots()

    inflection_point = compute_inflection_point(compute_throughput,
                                                memory_bandwidth)

    ax.plot([0, inflection_point], [0, compute_throughput], **kwargs)

    ax.hlines(compute_throughput,
              inflection_point,
              M*inflection_point,
              **kwargs)

    return ax
