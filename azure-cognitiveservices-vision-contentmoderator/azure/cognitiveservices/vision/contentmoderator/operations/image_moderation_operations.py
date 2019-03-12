# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse

from .. import models


class ImageModerationOperations(object):
    """ImageModerationOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def find_faces(
            self, cache_image=None, custom_headers=None, raw=False, **operation_config):
        """Returns the list of faces found.

        :param cache_image: Whether to retain the submitted image for future
         use; defaults to false if omitted.
        :type cache_image: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: FoundFaces or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.vision.contentmoderator.models.FoundFaces or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.contentmoderator.models.APIErrorException>`
        """
        # Construct URL
        url = self.find_faces.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if cache_image is not None:
            query_parameters['CacheImage'] = self._serialize.query("cache_image", cache_image, 'bool')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('FoundFaces', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    find_faces.metadata = {'url': '/contentmoderator/moderate/v1.0/ProcessImage/FindFaces'}

    def ocr_method(
            self, language, cache_image=None, enhanced=False, custom_headers=None, raw=False, **operation_config):
        """Returns any text found in the image for the language specified. If no
        language is specified in input then the detection defaults to English.

        :param language: Language of the terms.
        :type language: str
        :param cache_image: Whether to retain the submitted image for future
         use; defaults to false if omitted.
        :type cache_image: bool
        :param enhanced: When set to True, the image goes through additional
         processing to come with additional candidates.
         image/tiff is not supported when enhanced is set to true
         Note: This impacts the response time.
        :type enhanced: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: OCR or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.vision.contentmoderator.models.OCR or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.contentmoderator.models.APIErrorException>`
        """
        # Construct URL
        url = self.ocr_method.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['language'] = self._serialize.query("language", language, 'str')
        if cache_image is not None:
            query_parameters['CacheImage'] = self._serialize.query("cache_image", cache_image, 'bool')
        if enhanced is not None:
            query_parameters['enhanced'] = self._serialize.query("enhanced", enhanced, 'bool')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('OCR', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    ocr_method.metadata = {'url': '/contentmoderator/moderate/v1.0/ProcessImage/OCR'}

    def evaluate_method(
            self, cache_image=None, custom_headers=None, raw=False, **operation_config):
        """Returns probabilities of the image containing racy or adult content.

        :param cache_image: Whether to retain the submitted image for future
         use; defaults to false if omitted.
        :type cache_image: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Evaluate or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.vision.contentmoderator.models.Evaluate or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.contentmoderator.models.APIErrorException>`
        """
        # Construct URL
        url = self.evaluate_method.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if cache_image is not None:
            query_parameters['CacheImage'] = self._serialize.query("cache_image", cache_image, 'bool')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Evaluate', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    evaluate_method.metadata = {'url': '/contentmoderator/moderate/v1.0/ProcessImage/Evaluate'}

    def match_method(
            self, list_id=None, cache_image=None, custom_headers=None, raw=False, **operation_config):
        """Fuzzily match an image against one of your custom Image Lists. You can
        create and manage your custom image lists using <a
        href="/docs/services/578ff44d2703741568569ab9/operations/578ff7b12703741568569abe">this</a>
        API.
        Returns ID and tags of matching image.<br/>
        <br/>
        Note: Refresh Index must be run on the corresponding Image List before
        additions and removals are reflected in the response.

        :param list_id: The list Id.
        :type list_id: str
        :param cache_image: Whether to retain the submitted image for future
         use; defaults to false if omitted.
        :type cache_image: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: MatchResponse or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.vision.contentmoderator.models.MatchResponse
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.contentmoderator.models.APIErrorException>`
        """
        # Construct URL
        url = self.match_method.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if list_id is not None:
            query_parameters['listId'] = self._serialize.query("list_id", list_id, 'str')
        if cache_image is not None:
            query_parameters['CacheImage'] = self._serialize.query("cache_image", cache_image, 'bool')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('MatchResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    match_method.metadata = {'url': '/contentmoderator/moderate/v1.0/ProcessImage/Match'}

    def find_faces_file_input(
            self, image_stream, cache_image=None, custom_headers=None, raw=False, callback=None, **operation_config):
        """Returns the list of faces found.

        :param image_stream: The image file.
        :type image_stream: Generator
        :param cache_image: Whether to retain the submitted image for future
         use; defaults to false if omitted.
        :type cache_image: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param callback: When specified, will be called with each chunk of
         data that is streamed. The callback should take two arguments, the
         bytes of the current chunk of data and the response object. If the
         data is uploading, response will be None.
        :type callback: Callable[Bytes, response=None]
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: FoundFaces or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.vision.contentmoderator.models.FoundFaces or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.contentmoderator.models.APIErrorException>`
        """
        # Construct URL
        url = self.find_faces_file_input.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if cache_image is not None:
            query_parameters['CacheImage'] = self._serialize.query("cache_image", cache_image, 'bool')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'image/gif'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._client.stream_upload(image_stream, callback)

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('FoundFaces', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    find_faces_file_input.metadata = {'url': '/contentmoderator/moderate/v1.0/ProcessImage/FindFaces'}

    def find_faces_url_input(
            self, content_type, cache_image=None, data_representation="URL", value=None, custom_headers=None, raw=False, **operation_config):
        """Returns the list of faces found.

        :param content_type: The content type.
        :type content_type: str
        :param cache_image: Whether to retain the submitted image for future
         use; defaults to false if omitted.
        :type cache_image: bool
        :param data_representation:
        :type data_representation: str
        :param value:
        :type value: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: FoundFaces or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.vision.contentmoderator.models.FoundFaces or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.contentmoderator.models.APIErrorException>`
        """
        image_url = models.BodyModel(data_representation=data_representation, value=value)

        # Construct URL
        url = self.find_faces_url_input.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if cache_image is not None:
            query_parameters['CacheImage'] = self._serialize.query("cache_image", cache_image, 'bool')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        # Construct body
        body_content = self._serialize.body(image_url, 'BodyModel')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('FoundFaces', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    find_faces_url_input.metadata = {'url': '/contentmoderator/moderate/v1.0/ProcessImage/FindFaces'}

    def ocr_url_input(
            self, language, content_type, cache_image=None, enhanced=False, data_representation="URL", value=None, custom_headers=None, raw=False, **operation_config):
        """Returns any text found in the image for the language specified. If no
        language is specified in input then the detection defaults to English.

        :param language: Language of the terms.
        :type language: str
        :param content_type: The content type.
        :type content_type: str
        :param cache_image: Whether to retain the submitted image for future
         use; defaults to false if omitted.
        :type cache_image: bool
        :param enhanced: When set to True, the image goes through additional
         processing to come with additional candidates.
         image/tiff is not supported when enhanced is set to true
         Note: This impacts the response time.
        :type enhanced: bool
        :param data_representation:
        :type data_representation: str
        :param value:
        :type value: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: OCR or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.vision.contentmoderator.models.OCR or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.contentmoderator.models.APIErrorException>`
        """
        image_url = models.BodyModel(data_representation=data_representation, value=value)

        # Construct URL
        url = self.ocr_url_input.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['language'] = self._serialize.query("language", language, 'str')
        if cache_image is not None:
            query_parameters['CacheImage'] = self._serialize.query("cache_image", cache_image, 'bool')
        if enhanced is not None:
            query_parameters['enhanced'] = self._serialize.query("enhanced", enhanced, 'bool')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        # Construct body
        body_content = self._serialize.body(image_url, 'BodyModel')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('OCR', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    ocr_url_input.metadata = {'url': '/contentmoderator/moderate/v1.0/ProcessImage/OCR'}

    def ocr_file_input(
            self, language, image_stream, cache_image=None, enhanced=False, custom_headers=None, raw=False, callback=None, **operation_config):
        """Returns any text found in the image for the language specified. If no
        language is specified in input then the detection defaults to English.

        :param language: Language of the terms.
        :type language: str
        :param image_stream: The image file.
        :type image_stream: Generator
        :param cache_image: Whether to retain the submitted image for future
         use; defaults to false if omitted.
        :type cache_image: bool
        :param enhanced: When set to True, the image goes through additional
         processing to come with additional candidates.
         image/tiff is not supported when enhanced is set to true
         Note: This impacts the response time.
        :type enhanced: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param callback: When specified, will be called with each chunk of
         data that is streamed. The callback should take two arguments, the
         bytes of the current chunk of data and the response object. If the
         data is uploading, response will be None.
        :type callback: Callable[Bytes, response=None]
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: OCR or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.vision.contentmoderator.models.OCR or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.contentmoderator.models.APIErrorException>`
        """
        # Construct URL
        url = self.ocr_file_input.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['language'] = self._serialize.query("language", language, 'str')
        if cache_image is not None:
            query_parameters['CacheImage'] = self._serialize.query("cache_image", cache_image, 'bool')
        if enhanced is not None:
            query_parameters['enhanced'] = self._serialize.query("enhanced", enhanced, 'bool')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'image/gif'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._client.stream_upload(image_stream, callback)

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('OCR', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    ocr_file_input.metadata = {'url': '/contentmoderator/moderate/v1.0/ProcessImage/OCR'}

    def evaluate_file_input(
            self, image_stream, cache_image=None, custom_headers=None, raw=False, callback=None, **operation_config):
        """Returns probabilities of the image containing racy or adult content.

        :param image_stream: The image file.
        :type image_stream: Generator
        :param cache_image: Whether to retain the submitted image for future
         use; defaults to false if omitted.
        :type cache_image: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param callback: When specified, will be called with each chunk of
         data that is streamed. The callback should take two arguments, the
         bytes of the current chunk of data and the response object. If the
         data is uploading, response will be None.
        :type callback: Callable[Bytes, response=None]
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Evaluate or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.vision.contentmoderator.models.Evaluate or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.contentmoderator.models.APIErrorException>`
        """
        # Construct URL
        url = self.evaluate_file_input.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if cache_image is not None:
            query_parameters['CacheImage'] = self._serialize.query("cache_image", cache_image, 'bool')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'image/gif'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._client.stream_upload(image_stream, callback)

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Evaluate', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    evaluate_file_input.metadata = {'url': '/contentmoderator/moderate/v1.0/ProcessImage/Evaluate'}

    def evaluate_url_input(
            self, content_type, cache_image=None, data_representation="URL", value=None, custom_headers=None, raw=False, **operation_config):
        """Returns probabilities of the image containing racy or adult content.

        :param content_type: The content type.
        :type content_type: str
        :param cache_image: Whether to retain the submitted image for future
         use; defaults to false if omitted.
        :type cache_image: bool
        :param data_representation:
        :type data_representation: str
        :param value:
        :type value: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Evaluate or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.vision.contentmoderator.models.Evaluate or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.contentmoderator.models.APIErrorException>`
        """
        image_url = models.BodyModel(data_representation=data_representation, value=value)

        # Construct URL
        url = self.evaluate_url_input.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if cache_image is not None:
            query_parameters['CacheImage'] = self._serialize.query("cache_image", cache_image, 'bool')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        # Construct body
        body_content = self._serialize.body(image_url, 'BodyModel')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Evaluate', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    evaluate_url_input.metadata = {'url': '/contentmoderator/moderate/v1.0/ProcessImage/Evaluate'}

    def match_url_input(
            self, content_type, list_id=None, cache_image=None, data_representation="URL", value=None, custom_headers=None, raw=False, **operation_config):
        """Fuzzily match an image against one of your custom Image Lists. You can
        create and manage your custom image lists using <a
        href="/docs/services/578ff44d2703741568569ab9/operations/578ff7b12703741568569abe">this</a>
        API.
        Returns ID and tags of matching image.<br/>
        <br/>
        Note: Refresh Index must be run on the corresponding Image List before
        additions and removals are reflected in the response.

        :param content_type: The content type.
        :type content_type: str
        :param list_id: The list Id.
        :type list_id: str
        :param cache_image: Whether to retain the submitted image for future
         use; defaults to false if omitted.
        :type cache_image: bool
        :param data_representation:
        :type data_representation: str
        :param value:
        :type value: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: MatchResponse or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.vision.contentmoderator.models.MatchResponse
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.contentmoderator.models.APIErrorException>`
        """
        image_url = models.BodyModel(data_representation=data_representation, value=value)

        # Construct URL
        url = self.match_url_input.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if list_id is not None:
            query_parameters['listId'] = self._serialize.query("list_id", list_id, 'str')
        if cache_image is not None:
            query_parameters['CacheImage'] = self._serialize.query("cache_image", cache_image, 'bool')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        # Construct body
        body_content = self._serialize.body(image_url, 'BodyModel')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('MatchResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    match_url_input.metadata = {'url': '/contentmoderator/moderate/v1.0/ProcessImage/Match'}

    def match_file_input(
            self, image_stream, list_id=None, cache_image=None, custom_headers=None, raw=False, callback=None, **operation_config):
        """Fuzzily match an image against one of your custom Image Lists. You can
        create and manage your custom image lists using <a
        href="/docs/services/578ff44d2703741568569ab9/operations/578ff7b12703741568569abe">this</a>
        API.
        Returns ID and tags of matching image.<br/>
        <br/>
        Note: Refresh Index must be run on the corresponding Image List before
        additions and removals are reflected in the response.

        :param image_stream: The image file.
        :type image_stream: Generator
        :param list_id: The list Id.
        :type list_id: str
        :param cache_image: Whether to retain the submitted image for future
         use; defaults to false if omitted.
        :type cache_image: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param callback: When specified, will be called with each chunk of
         data that is streamed. The callback should take two arguments, the
         bytes of the current chunk of data and the response object. If the
         data is uploading, response will be None.
        :type callback: Callable[Bytes, response=None]
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: MatchResponse or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.vision.contentmoderator.models.MatchResponse
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.contentmoderator.models.APIErrorException>`
        """
        # Construct URL
        url = self.match_file_input.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if list_id is not None:
            query_parameters['listId'] = self._serialize.query("list_id", list_id, 'str')
        if cache_image is not None:
            query_parameters['CacheImage'] = self._serialize.query("cache_image", cache_image, 'bool')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'image/gif'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._client.stream_upload(image_stream, callback)

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('MatchResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    match_file_input.metadata = {'url': '/contentmoderator/moderate/v1.0/ProcessImage/Match'}
