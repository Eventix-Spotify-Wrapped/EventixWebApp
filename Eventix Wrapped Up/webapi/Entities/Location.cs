namespace Eventix_Wrapped_Up.Entities
{
    public class Location
    {
        private float latitude;
        private float longitude;
        private int count;

        public Location(float latitude, float longitude, int count)
        {
            this.latitude = latitude;
            this.longitude = longitude;
            this.count = count;
        }
    }
}
