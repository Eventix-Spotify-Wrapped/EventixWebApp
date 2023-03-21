namespace Eventix_Wrapped_Up.Entities
{

    public class User
    {
        private string uuid;
        private string name;
        private string password;
        private string email;
        private string phone;

        public User()
        {
            
        }
        public User(string uuid, string name, string password, string email, string phone)
        {
            this.uuid = uuid;
            this.name = name;
            this.password = password;
            this.email = email;
            this.phone = phone;
        }

        public User(string name, string password, string email, string phone)
        {
            this.name = name;
            this.password = password;
            this.email = email;
            this.phone = phone;
        }
    }
}
