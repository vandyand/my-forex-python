import json


class EAParams():
    def __init__(self, pair, units, short_ma, long_ma):
        self.pair = pair
        self.units = units
        self.short_ma = short_ma
        self.long_ma = long_ma

    def __repr__(self):
        return str(vars(self))

    @classmethod
    def from_file_ob(cls, ob):
        return EAParams(ob['pair'], ob['units'], ob['short_ma'], ob['long_ma'])

    @classmethod
    def load_ea_params(cls):
        data = json.loads(open('ea_params.json', 'r').read())
        return {k: cls.from_file_ob(v) for k, v in data.items()}

    @classmethod
    def get_pairs(cls):
        return list(cls.load_ea_params().keys())


if __name__ == "__main__":
    [print(k, v) for k, v in EAParams.load_ea_params().items()]
    print(EAParams.get_pairs())
