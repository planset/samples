using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Authorization;

namespace WebApplication4.Controllers
{
    [Route("api/[controller]")]
    [Authorize]
    public class RequiredAuthValuesController : Controller
    {
        // GET api/values
        [HttpGet]
        public IEnumerable<Hero> Get()
        {
            var heros = new List<Hero>();
            heros.Add(new Hero { Id = 3, Name = "test3" });
            heros.Add(new Hero { Id = 2, Name = "test2" });
            return heros;
        }

        // GET api/values/5
        [HttpGet("{id}")]
        public string Get(int id)
        {
            return "value";
        }

        // POST api/values
        [HttpPost]
        public void Post([FromBody]string value)
        {
        }

        // PUT api/values/5
        [HttpPut("{id}")]
        public void Put(int id, [FromBody]string value)
        {
        }

        // DELETE api/values/5
        [HttpDelete("{id}")]
        public void Delete(int id)
        {
        }
    }
}
