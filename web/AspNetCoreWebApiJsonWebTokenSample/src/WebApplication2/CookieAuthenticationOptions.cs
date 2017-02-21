namespace WebApplication2
{
    internal class CookieAuthenticationOptions
    {
        public string AuthenticationScheme { get; set; }
        public bool AutomaticAuthenticate { get; set; }
        public bool AutomaticChallenge { get; set; }
        public string CookieName { get; set; }
        public object TicketDataFormat { get; set; }
    }
}