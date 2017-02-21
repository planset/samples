using DevTrends.MvcDonutCaching;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace AspNetMvcDonutOutputCacheSample.Controllers
{
    public class HomeController : Controller
    {
        [DonutOutputCache(
            Duration = 10
            )]
        public ActionResult Index()
        {
            ViewBag.Title = "Home Page";

            return View();
        } 

        [DonutOutputCache(
            Duration = 10
            )]
        public JsonResult Get()
        {
            return this.Json(new { now = DateTime.Now.ToString() },JsonRequestBehavior.AllowGet);
        }


    }
}
