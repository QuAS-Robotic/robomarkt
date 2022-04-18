from abc import ABC, abstractmethod, abstractproperty

from core.utils.validator_errors import RunValidationError, ValidationError


class AbstractValidator(ABC):
    """
    Very similar to rest serializers but simpler.
    validation_rule is a dict. Key is validation func name and Value is kwargs for this func
    """

    @abstractproperty
    def errors():
        raise NotImplementedError

    @abstractproperty
    def validated_data():
        raise NotImplementedError

    @abstractmethod
    def is_valid(raise_exception=True):
        raise NotImplementedError
    
    @abstractmethod
    def run_validation():
        raise NotImplementedError


class BaseValidator(AbstractValidator):

    def __init__(self, data, validation_rules:dict, *args, **kwargs):
        self._initial_data = data
        self._validation_rules = validation_rules
        self.context = kwargs.pop("context", {})

    def is_valid(self, raise_exception=True):
        try:
            self._validated_data = self.run_validation(self.initial_data)
        except RunValidationError as exc:
            self._validated_data = []
            self._errors = exc.detail
        else:
            self._errors = []
        if self._errors and raise_exception:
            raise ValidationError(self.errors)  # TODO
        
        return not bool(self._errors)
    
    def run_validation(self):
        validated_data = type(self._initial_data)()

        for validation_func_name, func_kwargs in self.validation_rules:
            data_key = self._parse_data_key_from_func_name(validation_func_name)
            valitadion_func = getattr(self, validation_func_name)

            try:
                validated_datum = valitadion_func(**func_kwargs)
                validated_data = self._append_validated_data(validated_data=validated_data,
                                                             validated_datum=validated_datum, 
                                                             data_key=data_key)
            except ValidationError as err:
                self.__append_error(err)
        return validated_data

    @property
    def validated_data(self):
        return self._validated_data  
    @property
    def errors(self):
        return self._errors  

    def __append_error(self, error):
        assert isinstance(error, dict)
        self._error.extend(error)
    
    def _parse_data_key_from_func_name(validation_func_name, prefix="validate_", *args, **kwargs):
        return validation_func_name.split(prefix)[-1]
    
    def _append_validated_data(validated_data, validated_datum, *args, **kwargs):
        data_key = kwargs["data_key"]
        validated_data[data_key] = validated_datum
        return validated_data