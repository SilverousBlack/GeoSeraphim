import GeoSeraphim.Core as gsc

class GeoData(gsc.ResultType):
    __output_type__ = gsc.SYSDB.SYSTEM_CONFIGURATION["output"]
    
    def __init__(self, **kwargs):
        super(GeoData, self).__init__(**kwargs)
        
    def interpret(self, buf):
        pass

buf = GeoData(name="ibr")
print(buf)
