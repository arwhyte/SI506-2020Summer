import json
import requests


# 0.1 TEXT CONVENTIONS: References in the comments to classes, functions, variables, arguments, and
# file names are bounded by '<' name '>' as an aid to identification. Drop the '<' and '>' when
# using the names in your code.

print(f"\nStart SI 506 waiver exam\n")

# 1.0 Setup

print(f"Start section 1.0")

# 1.1 Requests module

# 1.1.1 Confirm, install or update the third-party requests package.

# Check
# Mac: $ python3 -m pip list | grep requests
# Win: $ python -m pip list | findstr requests

# Install
# Mac: $ python3 -m pip install requests
# Win: $ python -m pip install requests

# Update
# Mac: $ python3 -m pip install --upgrade requests
# Win: $ python -m pip install --upgrade requests

# 1.2 API ENDPOINT

# 1.2.1 The flickr API endpoint is provided below and assigned to the constant BASE_URL. Please
# do not change this value.

BASE_URL = 'https://api.flickr.com/services/rest/'

# 1.3 FLICKR KEY

# 1.3.1 If you do not have a flickr account create one per the sign up directions:
# https://help.flickr.com/en_us/sign-up-for-a-flickr-account-B1Mc3mskX

# 1.3.2 Once you have activated your account apply for a NON-COMMERCIAL flickr API KEY
# https://www.flickr.com/services/apps/create/apply

# 1.3.3 Provide a name for this script, e.g., "si506_waiver", provide a short description, click the
# acknowledgement checkboxes and then click SUBMIT.

# 1.3.4 assign your API key string value to the constant FLICKR_KEY.

FLICKR_KEY = None # TODO replace

# WARN: as a general rule do not share your API keys with others. In this case we need to
# test your setup so include the key value in your submission. Once we have scored your submission
# we recommend that you delete the "app" (which deletes the associated API key) and apply for a new
# non-commercial flickr API key.

# 1.4 CACHE FILE

# 1.4.1 The cache file name is provided below and assigned to the constant CACHE_FNAME. Please
# do not change this value.

CACHE_FNAME = 'stu_cached_data.json'

# HINT: if you happen to save data in this file that is wrong, just delete the file and re-run your
# program to regenerate < stu_cached_data.json >.

print(f"End section 1.0\n")


# 2.0 READING FILES

print(f"Start section 2.0")

# 2.1 This exam includes a number of local JSON files that you will need to read at various stages
# in the exercise in order to access data contained therein. To avoid code duplication and encourage
# re-use, implement a function named < read_json(filepath) > with a single positional parameter.

# The function will accept a filepath or filename provided by the caller in order to open the
# corresponding JSON file in read mode and return a file object. The function MUST then call the
# json module's load method in order to decode the file object and return it to the caller as a list
# or dictionary.

# Read the Docstring for guidance on implementing the function. It can be implemented with three (3)
# lines of code.

# 2.1.1 CONFIG: You MUST set the built-in open() function's optional parameter value as specified:
# encoding='utf-8'


def read_json(filepath):
    """Reads a JSON document and returns a list or dictionary if provided with
    a valid filepath.

    Parameters:
        filepath (str): path to file.

    Returns:
        dict or list: dictionary or list representations of the decoded JSON document.
    """

    pass # TODO replace


# 2.2 Call the function < read_json(filepath) > and pass to the filepath string
# < 'sample_flickr_photo_info.json' > as an argument. Assign the return value to the variable named
# < photo_thames_lit >. Review the JSON file after you have generated it.

photo_thames_lit = None # TODO replace

# 2.2.1 REVIEW: the file 'sample_flickr_photo_info.json' provides a JSON representation of a flickr
# photo. Take a moment to review the object structure and key-value pairs. You will work with this
# data structure later in the exam.

print(f"End section 2.0\n")


# 3.0 WRITING TO FILES

print(f"Start section 3.0")

# 3.1 Writing data to files is a common task that we expect you to know. To this end, implement the
# function named < write_json() > with two positional parameters. The function definition MUST
# include the following two parameters:

# < filepath >
# < data >

# In other words, the function will require two arguments supplied by the caller: 1) a string
# representing a filepath or filename and 2) a data object such as a list or dictionary containing
# list elements or dictionary key-value pairs that are serializable as JSON.

# The function code block will open the specified JSON file in write mode and return a file
# object. The function MUST then pass both the file object and the data payload to the json module's
# dump method in order to encode the data as JSON and write it to the target file.

# Read the Docstring for guidance on implementing the function. It can be implemented with two (2)
# lines of code.

# HINT: use a < with > statement in conjunction with the builtin function < open() > to access the
# file and return a file object.

# 3.1.1 CONFIG: You MUST set the built-in open() function's optional encoding parameter value as
# specified: encoding='utf-8'

# 3.1.2 CONFIG: You MUST set the following json.dump() optional parameter values as specified:
# ensure_ascii=False
# indent=2


def write_json(): # TODO fix
    """Given a valid filepath writes encodes data as JSON and writes it to a JSON file.

    Parameters:
        filepath (str): the path to the file.
        data (dict): the data to be encoded as JSON and written to the file.

    Returns:
        None
    """

    pass # TODO replace


# 3.2 As a warmup, create a dictionary named < photo > with data from the dictionary < photo_thames_lit >. 
# The dictionary MUST include the followings keys:

# < id > (str) the photo id
# < title > (str) title _content
# < tags > (list) tag _content
# < owner > (str) owner's username

# For each < photo > key assign the corresponding value found in < photo_thames_lit >.

# HINT: you MUST loop over the tags and append each tag < _content > value to a list which you will
# then assign to the < tags > key.

photo = None # TODO replace

# 3.3 Call the function write_json(filepath, data) and pass to it as arguments the filepath string
# 'stu_photo_thames_lit.json' and the dictionary named < photo >.

write_json(None, None) # TODO replace

print(f"End section 3.0\n")


# 4.0 WORKING WITH LISTS AND DICTIONARIES

print(f"Start section 4.0")

# 4.1 Now demonstrate that you are comfortable working with lists and dictionaries. Call the
# function < read_json(filepath) > and pass to it as an argument the filepath string
# < 'sample_flickr_response.json' >. Assign the return value to the variable named
# < sample_response >. Review the JSON file after you have generated it.

sample_response = None # TODO replace

# 4.2 Implement the utility function < get_photos(data) >. Call this function when you need to
# retrieve a list of photos (e.g., photos) from a flickr response. Read the Docstring for guidance
# on implementing the function. It can be implemented with one (1) line of code.


def get_photos(data):
    """Returns list of 'photo' dictionaries extracted from the passed in flickr response object.

    Parameters:
        data (dict): the flickr response object decoded as a dictionary.

    Returns:
        list: list of dictionaries that represent the photos included in the response.
    """

    pass # TODO replace


# 4.3 Call < get_photos(data) > and pass to it as an argument the dictionary < sample_response >.
# Assign the return value to a variable named < sample_photos >.

sample_photos = None # TODO replace

# 4.4 Return a count of the number of elements (i.e., photo records) in the list < sample_photos >.
# Assign the return value to a variable named < sample_photos_count >.

sample_photos_count = None # TODO replace

# 4.5 Use negative list slicing notation to return the last twelve (12) elements
# (i.e., photo records) up to but EXCLUDING the final element in the list
# < sample_photos >. Assign the return value to a variable named < sample_photos_slice >.

sample_photos_slice = None # TODO replace

# 4.6 Write a for loop or list comprehension that loops over the list < sample_photos > and returns
# a list of 'photo' dictionaries that contain the word 'bridge' in the title. The conditional
# expression you write MUST be case-insentive (i.e., it must filter on either 'bridge' or 'Bridge').
# Assign the return value to a variable named < bridge_sample_photos >.

sample_photos_bridge = None # TODO replace

# 4.7 Write a for loop that loops over the list < sample_photos >, checks
# the < server > value (i.e., server number) of each photo record, identifies the range of server
# numbers within which the server number falls as per the keys specified in the dictionary
# < server_group_counts > (e.g., '4000_to_4099'), and increments the 'group' value by one (1).
# The goal is to obtain updated server counts across the three server groups specified in the
# dictionary plus 'other'.

server_group_counts = {
    '4000_to_4099': 0,
    '4100_to_4199': 0,
    '4200_to_4299': 0,
    'other': 0
}

# TODO write for loop or list comprehension to update < server_group_counts >

# 4.8 Implement the utility function < get_photo_ids(data) >. Call this function when you need to
# retrieve a list of photo ids from a flickr response. Write a for loop or list comprehension to
# to iterate over the photos and return a list of ids.

# Read the Docstring for guidance on implementing the function. It can be implemented with less
# than five (5) lines of code.


def get_photo_ids(data):
    """Returns a list of photo ids extracted from the passed in flickr response object. Calls
    get_photos(data) to return list of photo dictionaries. Extracts individual photo ids by looping
    over the photo list and appending each id to a new list that is returned to the caller.

    HINT: Write a for loop or list comprehension that iterates over the 'photo' list returned by
    < get_photos(data) > and appends each photo's id to the a new list (accumulator pattern).

    Parameters:
        data (dict): the flickr response object decoded as a dictionary.

    Returns:
        list: list of strings that represent the photo ids included in the response.
    """

    pass # TODO replace


# 4.9 Now call < get_photo_ids(data) > passing to it as an argument the list < sample_response >
# created above and assign the return value to a variable named < sample_photo_ids >.

sample_photo_ids = None # TODO replace

# 4.10 Call the function < write_json(filepath, data) > and pass to it the filepath string
# < 'stu_sample_photo_ids.json' > and the list named < sample_photo_ids > as arguments. Review the
# JSON file after you have generated it.

write_json(None, None) # TODO replace

print(f"End section 4.0\n")


# 5.0 SEARCH FLICKR

print(f"Start section 5.0")

# 5.1 Next you will implement three (3) functions designed to provide the following capabilities:

# < get_cache(filepath) > -- provides a simple caching mechanism for persisting flickr API response
# data and eliminating duplicate HTTP GET requests.

# < get_resource(url, params=None, timeout=20) > -- handles HTTP GET requests using the requests
# module.

# < get_flickr_resource(url, params) > -- manages the data request workflow, including cache item
# management and API requests.

# The goal is to implement a set of functions that provide a common workflow for querying the flickr
# API, caching responses, and using cached data in order to reduce the number of API calls required
# to retrieve data (occasionally an expensive operation).

# 5.2 Two additional functions are provided for your use. Please do not modify or remove these
# functions.

# < create_cache_id(url, params, private_keys=["api_key"]) > -- creates keys for cached items.

# < create_photo_search_params(api_key, tag, num=50) > -- creates a dictionary of parameters
# to be transmitted to the flickr API endpoint when conducting a photo search.

# NOTE: A more advanced implementation might refactor < get_flickr_resource(url, params) > as
# < get_flickr_resource(url, **kwargs) > passing to it a keyworded variable-length argument list
# using the < *kwargs > syntax for the various parameters that flickr API needs to process a
# request but that feature of the Python language is out-of-scope for SI 506.

# 5.2.1 Provided function. Do NOT modify.


def create_cache_item_id(url, params, private_keys=["api_key"]):
    """Returns a synthetic key composed of the API endpoint URL plus keys and values concatenated
    together for items added to the < simple_cache >.

    Parameters:
        url (str): API endpoint.
        params (dict): Dictionary of key-value pairs required for a flickr search operation.
        private_keys (list): key_value pairs to be excluded when constructing the cache_id.

    Returns:
        str: synthetic key used to identify a cached item.
    """

    sorted_keys = sorted(params.keys())
    res = []

    for key in sorted_keys:
        if key not in private_keys:
            res.append(f"{key}-{params[key]}")

    cache_id = url + "_".join(res)

    return cache_id


# 5.2.2 Provided function. Do NOT modify.


def create_photo_search_params(api_key, tag, num=50):
    """Returns a dictionary of key-value pairs comprising the search parameters required by the
    flickr API method flickr.photos.search.

    Parameters:
        api_key (str): User's flickr API key.
        tag (str): search term.
        num (int): max number of records to be returned (default = 50).

    Returns:
        dict: Dictionary of key-value pairs required for a flickr search operation.
    """

    return {
        'api_key': api_key,
        'format': 'json',
        'method': 'flickr.photos.search',
        'nojsoncallback': 1,
        'per_page': num,
        'tags': tag,
        'tag_mode': 'all'
    }


# 5.3 Implement the utility function < get_cache(filepath) >. Call this function to retrive the
# cache file, if it exists. Otherwise return an empty dictionary.

# Read the Docstring for guidance on implementing the function. It can be implemented with less
# than five (5) lines of code.

# HINT: implement try and except blocks to handle calling read_json(filepath) and passing in
# a < filepath > to a (non-existent) file that has yet to be created.


def get_cache(filepath):
    """Calls read_json(filepath) to open cache file. If cache file does not exist, returns an empty
    dictionary rather than raising a runtime exception.

    Parameters:
        filepath (str): path to cache file.

    Returns:
        dict: cached dictionary of data if cache file exists or an empty dictionary if cache file
              not located.
    """

    pass # TODO replace


# 5.4 Implement the utility function < get_resource(url, params=None, timeout=20) >. Call this
# function to issue HTTP GET requests using the requests module.

# Read the Docstring for guidance on implementing the function. It can be implemented with less
# than six (6) lines of code.


def get_resource(url, params=None, timeout=20):
    """Initiates an HTTP GET request in order to return a representation of a resource. The
    function defines three parameters: the resource URL (str), an optional params (dict) of
    key:value pairs that form the provided URL's querystring, and an optional timeout value
    (in seconds). If no params are provided the request is made without specifying any params.
    Calls the request module's json() method in order to decode the response JSON as a
    dictionary prior to returning the response.

    Parameters:
        url (str): a url that specifies the resource.
        params (dict): optional dictionary of querystring arguments.
        timeout (int): timeout value in seconds. Default value is 20 seconds.

    Returns:
        dict: dictionary representation of the decoded JSON.
    """

    pass # TODO replace


# 5.5 Implement the function < get_flickr_resource(url, params) >. This function manages the data
# request workflow, including cache item management and API requests.

# The required workflow is as follows:

# 1. Create cache item id: calls < create_cache_item_id(url, params) > returning unique id based on
#    passed in < url > and < params > arguments and assigns return value to a local
#    < cache_item_id > variable.
# 2. Get cache: calls get_cache(filepath) and assigns the return value to a local
#    < simple_cache > variable (if no cache file exists get_cache(filepath) returns an empty
#    dictionary).
# 3. Locate item in cache: checks for matching cached item by < cache_item_id > and, if located,
#    returns the matched cache item to the caller (i.e., returns value and EXITS function).

# If item is not found in the cache, the workflow continues with the function performing the
# following tasks:

# 4. Issue request: if item is NOT located in the cache issues an HTTP GET request to retrieve the
#    resource from the API endpoint by calling < get_resource(url, params) >.
# 5. Add item to cache: assigns return value of API call to cache using the < cache_item_id > as
#    the key.
# 6. Update cache: calls write_json(filepath, data), which updates (overwrites) the existing cache
#    file or creates a new cache file if none exists.
# 7. Return response: returns API response to the caller and EXITS function.

# Read the Docstring for guidance on implementing the function. It can be implemented in
# under ten (10) lines of code.

# HINT: Remember that we already established the cache file name in 1.4


def get_flickr_resource(url, params):
    """ Creates a local < cache_item_id > based on passed in < url > and < params > arguments.
    Retrieves cache and checks for existing cached item using local < cache_item_id >. If matching
    cache item is found, returns the cached item to the caller.

    If item is NOT located in the cache issues an HTTP GET request to retrieve the resource from
    the API endpoint. Assigns return value of API call to cache using < cache_item_id > as the key.
    This action updates (overwrites) the existing cache file or creates a new cache file if none
    exists. After cache is overwritten, returns the API response to the caller.

    Parameters:
        url (str): API endpoint URL
        params (dict): dictionary of key-value pairs required by the API for processing the request

    Returns:
        dict: API response decoded to a dictionary
    """

    pass # TODO replace


# 5.6 Now let's request a resource from the flickr API. Assuming the above functions are
# implemented call < create_photo_search_params(key, tag, num=50) > passing to the function your
# < FLICKR_KEY >, the string < 'mountain' >, and < num=25 > (i.e., the number of
# photos to be returned) as arguments. Assign the return value to a variable named
# < mountain_params >. These are the parameters that you will transmit to the flickr API when you
# issue your HTTP GET request.

mountain_params = None # TODO replace

# 5.7 Call get_flickr_resource(url, params) to issue the HTTP GET request, passing to the function
# the < BASE_URL > and < params > as arguments. Assign the return value to a variable named
# < mountains >.

mountains = None # TODO replace

# 5.8 Call the utility function < get_photos(data) > passing to the function < mountains > as the
# argument. Assign the return value to a variable named < mountain_photos >.

mountain_photos = None # TODO replace

# 5.9 Call the function < write_json(filepath, data) > and pass to it the filepath string
# < 'stu_mountain_photos.json' > and the list < mountain_photos > as arguments. Review
# the JSON file after you have generated it.

write_json(None, None) # TODO replace

# 5.10 Call the function < get_photo_ids(data) > passing to the function < mountains > as the
# argument. Assign the return value to a variable named < mountain_photo_ids >.

mountain_photo_ids = None # TODO replace

# 5.11 Call the function write_json(filepath, data) and pass to it the filepath string
# < 'stu_flickr_mountain_photo_ids.json' > and the list < mountain_photo_ids > as arguments.
# Review the JSON file after you have generated it.

write_json(None, None) # TODO replace

print(f"End section 5.0\n")


# 6.0 GET FLICKR PHOTO INFO

print(f"Start section 6.0")

# 6.1 The flickr API allows users to request information (metadata) about each photo in its
# collection. In order to retrieve this data you will need to transmit a set of key-value pairs that
# differ from the remote photo search you conducted above.

# To simplify assembling the key-value pairs to be sent to the flickr API for processing, implement
# the function < create_photo_info_params() > with two positional parameters. The function
# definition MUST include the following two parameters:

# < api_key >
# < photo_id >

# In other words, the function will require two arguments supplied by the caller: 1) the
# caller's flickr key and 2) the unique identifier of a photo about which more information is
# needed.

# The function will return to the caller a dictionary containing the following key value pairs:

# < api_key > (str) user's flickr API key (passed in by caller)
# < format > (str) response format. Set value to 'json'.
# < method > (str): flickr API method. Set value to 'flickr.photos.getInfo'.
# < nojsoncallback > (int) set value to 1.
# < photo_id > (str) flickr photo unique id (passed in by caller).

# Read the Docstring for guidance on implementing the function. It can be implemented in under seven
# (7) lines of code.

# HINT: The function design is similar to < create_photo_search_params(api_key, tag, num=50) >.


def create_photo_info_params(): # TODO fix
    """Returns a dictionary of key-value pairs comprising the photo parameters required by the
    flickr API method flickr.photos.getInfo.

    Parameters:
        api_key (str): User's flickr API key.
        photo_id (str): flickr photo unique identifier.

    Returns:
        dict: Dictionary of key-value pairs required for a flickr photo get info operation.
    """

    pass # TODO replace


# 6.2 Next, create an empty list named < sample_photos_info >. You will use it to accumulate 'photo'
# dictionaries containing photo metadata (see the file < sample_photo.json > for an example).
# Then loop over the list you created earlier named < sample_photo_ids >.
#
# During each loop iteration do the following:
#
# Call < create_photo_info_params(api_key, photo_id, num=50) > passing in your flickr api key
# and the id encountered (the default < num > limit does not need to be changed).
#
# Then call < get_flickr_resource(url, params) > passing to it the flickr API endpoint URL and the
# return value of < create_photo_info_params(api_key, photo_id) > (the "params").
#
# Append the dictionary return value of < get_flickr_resource(url, params) > to
# < sample_photos_info >.
#
# Repeat the above operations for each iteration of the loop.

sample_photos_info = None # TODO replace

# 6.3 Call the function < write_json(filepath, data) > and pass to it the filepath string
# < 'stu_sample_photos_info.json' > and the list < sample_photos_info > as arguments. Review the
# JSON file after you have generated it.

write_json(None, None) # TODO replace

print(f"End section 6.0\n")


# 7.0 WORKING WITH CLASS INSTANCES

print(f"Start section 7.0")

# 7.1 For the final section of the waiver exam, you will implement two classes that represent
# an individual photo and the owner of the photo. You will instantiate these classes to hold photo
# and owner information sourced from flickr. You will also implement three methods per class that
# will 1) simplify class instantiation with required instance variable values, 2) provide a string
# representation of the object, and 3) provide a dictionary representation of the object, the latter
# method providing a JSON-friendly representation of the object for file writing operations.

# 7.2 Create a class named < Person >. Design the class as follows:

# 7.2.1 Implement a 'dunder' < __init__() > method. The < init > method MUST be provisioned with
# paramaters that permit setting values for the following instance variables whenever a < Person >
# is instantiated:
#
# nsid (str)
# username (str)
# realname (str)
# location (str)

# HINT: the < nsid > instance variable value is a flickr photo owner's user id. See
# < sample_photo.json > for an example of how flickr represents an < owner >.

# 7.2.2 Implement a < jsonable() > method. The < jsonable > method MUST return a dictionary
# representation of a < Person > instance. The instance variable names will comprise the keys of the
# dictionary to be returned while the instance variable values will comprise the associated values.

# HINT: Calling the < jsonable() > method will return a JSON-friendly dictionary representation of
# the < Person > instance. The dictionary can then be passed as an argument to
# < write_json(filepath, data) >, encoded as JSON, and written to a file.

# 7.2.3 Implement a 'dunder' < __str__() > method. The < __str__() > method MUST return a string
# representation of the Person object. The following string format MUST be utilized:

# < realname > (nsid: < nsid >, username: < username >)


class Person:
    """ Representation of a Person.

    Attributes:
        nsid (str): unique identifier assigned to the user
        namename (str): username selected by user
        realname (str): name provided by user; usually first and last name
        location (str): user's location (if provided)

    Methods:
        jsonable: return JSON-friendly dictionary representation of the object.
    """

    def __init__(self): # TODO fix

        pass # TODO replace

    def jsonable(self):
        """Return a JSON-friendly representation of the object.
        Use a dictionary literal rather than built-in dict() to avoid
        built-in lookup costs.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variable values
        """

        pass # TODO replace

    def __str__(self):
        """String representation of the object."""

        pass # TODO replace


# 7.3 Create a class named < Photo >. Design the class as follows:

# 7.3.1 Implement the 'dunder' < __init__() > method. The < init > method MUST be provisioned with
# paramaters that permit setting values for the following instance variables whenever a < Photo >
# is instantiated:
#
# id (str)
# title (str)
# date_taken (str)
# tags (list of str)
# owner (Person)

# HINT: Assign an instance of < Person > to the < owner > instance variable.

# 7.3.2 Implement the get_web_page_url() method. The function MUST return a URL string that includes
# the owner's < nsid > value and the photo < id >. The format is as follows:

# URL format: https://www.flickr.com/photos/< owner nsid >/< photo id >

# 7.3.3 Implement the < jsonable() > method. The < jsonable > method MUST return a dictionary representation
# of a < Photo > instance. The instance variable names will comprise the keys of the dictionary to
# be returned while the instance variable values will comprise the associated values.

# HINT: Calling the < jsonable() > method will return a JSON-friendly dictionary representation of
# the < Photo > instance. The dictionary can then be passed as an argument to
# < write_json(filepath, data) >, encoded as JSON, and written to a file.

# 7.3.4 Implement the 'dunder' < __str__() > method. The < __str__() > method MUST return a string
# representation of the Person object. The following string format MUST be utilized:

# < title > (id: < id >, owner: < username >)


class Photo:
    """Representation of a photo.

     Attributes:
        id (str): unique identifier assigned to the photo
        title (str): title of photo provided by owner
        date_taken (str): date/time photo was taken
        tags (list): one or more string _content labels assigned to the photo
        owner (Person): owner of photo

    Methods:
        jsonable: return JSON-friendly dictionary representation of the object.
    """

    def __init__(self): # TODO fix

        pass # TODO replace

    def get_web_page_url(self):
        """Return the photo's web page URL.

        URL format: https://www.flickr.com/photos/< owner nsid >/< photo id >

        Parameters:
            None

        Returns:
            str: web page URL based on photo id and owner nsid
        """

        pass # TODO replace

    def jsonable(self):
        """Return a JSON-friendly representation of the object.
        Use a dictionary literal rather than built-in dict() to avoid
        built-in lookup costs.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variable values
        """

        pass # TODO replace

    def __str__(self):
        """String representation of the object."""

        pass # TODO replace


# 7.4 Once you've implemented the < Person > and < Photo > classes let's put them to work. Create
# an empty list called < sample_photo_instances >. Write a for loop or list comprehension that
# loops over the list < sample_photos_info >. During each loop iteration create an instance of
# of < Photo > and set the values of its instance variables to the appropriate dictionary values. In
# the case of the < owner > instance variable you will need to assign an instance of < Person >,
# setting its instance variables when you instantiate the object.

# HINT: Review < sample_photo_info.json > for the nested key-value pairs that you will be accessing.

# HINT: You will need to also loop over the tag list to populate the tags instance variable. You can
# do this with a second for loop or list comprehension.

# WARN: not all records in < sample_photos_info > contain a representation of a photo. Check
# the file < stu_sample_photos_info.json > by searching on the < stat > property for a value other than
# "ok" and then add a conditional statement to your loop that filters out the non-photo records.

sample_photo_instances = None # TODO replace

# 7.5 Loop over < sample_photo_instances >. Inside the loop block of code write a conditional
# statement that checks the photo owner's < nsid > and the photo <id> against the two provided
# values, testing both values for equality. If a match is found, call the photo instance's
# < get_web_page_url() > and assign the return value to the variable < web_page_url >. Then exit
# the loop.

owner_nsid = '50393970@N06'
photo_id = '35508953642'
web_page_url = None # TODO replace

# TODO write loop block of code

# 7.6 Unlike previous lists < sample_photos_instances > is populated with a list of < Photo >
# objects not dictionaries. The Python standard json library is not designed to encode custom
# objects like < Photo > and < Person > (it handles standard types well). If you attempt to pass
# the list to < write_json(filepath, data) > you will raise the following runtime exception:

# TypeError: Object of type Photo is not JSON serializable

# The workaround involves calling the two < jsonable() > methods you implemented in < Photo > and
# < Person > in order to return JSON-friendly dictionary representations of the two objects.

# Given this, write a simple for loop or list comprehension that populates a new list named
# < sample_photo_instances_jsonable > with dictionary representations of the < Photo > and
# < Person > objects that you are storing in < sample_photo_instances > (i.e., call each
# photo object's < jsonable() > method to return the dictionary).

sample_photo_instances_jsonable = None # TODO replace

# 7.7 Call the function write_json(filepath, data) and pass to it the filepath string
# < 'photo_instances_jsonable.json' > and the list < sample_photo_instances_jsonable > as arguments. Review the JSON
# file after you have generated it.

write_json(None, None) # TODO replace

# WARN: If during testing the following runtime errors are ecountered:

# TypeError: Object of type Photo is not JSON serializable
# or
# TypeError: Object of type Person is not JSON serializable

# recheck your implementation of both the < Photo > and < Person > < jsonable() > methods.
# In particular, review how you are handling the < owner > key value assignment in < Photo >
# < jsonable() >. Make sure the value assigned to the < owner > key is a dictionary
# representation of a < Person > and not a < Person > instance.

print(f"End section 7.0\n\nEnd SI 506 waiver exam\n")

# END SI 506 WAIVER EXAM
