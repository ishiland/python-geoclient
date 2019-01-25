class GeoclientError(Exception):
    def __init__(self, message, result=None):
        super(GeoclientError, self).__init__(message)
        self.result = result


def _format_return_message(results):
    """
    Formats and eliminates redundant return messages from a failed geocoding result.
    :param results: the returned dictionary from Geoclient API of a failed geocode.
    :return: Formatted Geoclient return messages
    """
    out_message = None

    if 'message' in results:
        out_message = results['message']

    if 'message2' in results:
        if out_message:
            if out_message != results['message2']:
                out_message = "{} {}".format(out_message, results['message2'])
        else:
            return results['message2']

    return out_message
