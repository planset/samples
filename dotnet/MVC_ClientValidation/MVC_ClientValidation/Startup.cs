using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(MVC_ClientValidation.Startup))]
namespace MVC_ClientValidation
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
