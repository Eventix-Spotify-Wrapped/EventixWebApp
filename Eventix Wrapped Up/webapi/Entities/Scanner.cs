namespace Eventix_Wrapped_Up.Entities
{
    public class Scanner
    {
        private string guid;
        private string name;
        private DateTime expired_at;

        public Scanner(string guid, string name, DateTime expired_at)
        {
            this.guid = guid;
            this.name = name;
            this.expired_at = expired_at;
        }
    }
}
