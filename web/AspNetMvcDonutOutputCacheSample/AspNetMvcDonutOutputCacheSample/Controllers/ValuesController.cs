using DevTrends.MvcDonutCaching;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;

namespace AspNetMvcDonutOutputCacheSample.Controllers
{
    public class ValuesController : ApiController
    {
        // GET api/values
        [DonutOutputCache( Duration = 10)]
        public IEnumerable<string> Get()
        {
            System.Diagnostics.Debug.WriteLine("Get");
            return new string[] { "value1", "value2" };
        }

        // GET api/values/5
        public string Get(int id)
        {
            return "value";
        }

        // POST api/values
        public void Post([FromBody]string value)
        {
        }

        // PUT api/values/5
        public void Put(int id, [FromBody]string value)
        {
        }

        // DELETE api/values/5
        public void Delete(int id)
        {
        }
    }
}
