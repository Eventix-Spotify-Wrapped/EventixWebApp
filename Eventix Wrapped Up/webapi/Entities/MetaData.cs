namespace Eventix_Wrapped_Up.Entities
{
    public class MetaData
    {
        private string guid;
        private string name;
        private string type;

        public MetaData(string guid, string name, string type)
        {
            this.guid = guid;
            this.name = name;
            this.type = type;
        }
    }
}
