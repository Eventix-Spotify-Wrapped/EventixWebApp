namespace Eventix_Wrapped_Up.Entities
{
    public class Ticket
    {
        private string guid;
        private string event_id;
        private string name;
        private int increment;

        public Ticket(string guid, string event_id, string name, int increment)
        {
            this.guid = guid;
            this.event_id = event_id;
            this.name = name;
            this.increment = increment;
        }
    }
}
