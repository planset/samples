namespace SQLSamples.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class FixColumnName : DbMigration
    {
        public override void Up()
        {
            AddColumn("dbo.Personnels", "child3", c => c.String());
            DropColumn("dbo.Personnels", "chidl3");
        }
        
        public override void Down()
        {
            AddColumn("dbo.Personnels", "chidl3", c => c.String());
            DropColumn("dbo.Personnels", "child3");
        }
    }
}
