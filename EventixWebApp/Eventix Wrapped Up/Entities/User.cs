

namespace Eventix_Wrapped_Up.Entities
{

    public class User
    {
        private string uuid;
        private string name;
        private string password;
        private string email;

        public User()
        {
            
        }
        public User(Guid uuid, string name, string password, string email)
        {
            uuid=Guid.NewGuid();
            this.uuid = uuid.ToString();
            this.name = name;
            this.password = password;
            this.email = email;     
        }

        public User(string name, string password, string email)
        {
            this.name = name;
            this.password = password;
            this.email = email;
        }
    }
}
