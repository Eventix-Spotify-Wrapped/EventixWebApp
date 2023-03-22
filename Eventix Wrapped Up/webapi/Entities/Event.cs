namespace Eventix_Wrapped_Up.Entities
{
    public class Event
    {
        private string uuid;
        private string name;
        private EventType type;
        private EventStatus status; // progress
        private string locale; //event locale (en_GB, etc.)
        private Currency currency;

        public Event(string uuid, string name, EventType type, EventStatus status, string locale, Currency currency)
        {
            this.uuid = uuid;
            this.name = name;
            this.type = type;
            this.status = status;
            this.locale = locale;
            this.currency = currency;
        }
    }

    public enum EventType
    {
        ONCE,
        REPEATING,
    }
    public enum EventStatus
    {
        UNAVAILABLE,
        AVAILABLE,
        SOLD_OUT,
        REFUNDING,
        MOVING,
    }
    public enum Currency
    {
        EUR,
        USD,
    }
}