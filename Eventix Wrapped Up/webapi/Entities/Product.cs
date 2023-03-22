namespace Eventix_Wrapped_Up.Entities
{
    public class Product
    {
        private string guid;
        private string event_id;
        private string name;
        private ProductType type;
        private float vat_percentage;

        public Product(string guid, string event_id, string name, ProductType type, float vat_percentage)
        {
            this.guid = guid;
            this.event_id = event_id;
            this.name = name;
            this.type = type;
            this.vat_percentage = vat_percentage;
        }
    }

    public enum ProductType
    {
        NORMAL,
        VARYING,
    }
}
