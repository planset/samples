using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Data;
using System.Data.Entity;
using System.Data.Entity.Migrations;

using System.Management.Automation;

namespace SQLSamples
{
    class Program
    {
        static void Main(string[] args)
        {
            Database.SetInitializer(
                new System.Data.Entity.MigrateDatabaseToLatestVersion<EFDbContext, Migrations.Configuration>());

            using(var db = new EFDbContext())
            {
                db.Database.ExecuteSqlCommand("TRUNCATE TABLE Personnels");
                db.Personnels.Add(new Personnel()
                {
                    employee = "赤井",
                    child1 = "一郎ほげ",
                    child2 = "二郎",
                    child3 = "三郎"
                });
                db.Personnels.Add(new Personnel()
                {
                    employee = "工藤",
                    child1 = "春子",
                    child2 = "夏子"
                });
                db.Personnels.Add(new Personnel()
                {
                    employee = "鈴木",
                    child1 = "夏子"
                });
                db.Personnels.Add(new Personnel()
                {
                    employee="吉田拓郎"
                });
                db.SaveChanges();

                var rows = db.Database.SqlQuery<PersonnelResult>(
                    " SELECT employee,child1 as child FROM personnels "
                   + " UNION ALL "
                   + " SELECT employee,child2 as child FROM personnels "
                   + " UNION ALL "
                   + " SELECT employee,child3 as child FROM personnels "
                   );

                //var s = TableFormatter.toFormatTable(rows);
                //System.Diagnostics.Trace.WriteLine(s);

                var ps = PowerShell.Create()
                    .AddCommand("Format-Table").AddArgument(rows.ToArray());
                //.AddCommand("Out-String");

                var r = ps.Invoke();

                Console.WriteLine(r[0]);

            }
        }
    }

    //public class Hoge: System.Management.Automation.PSCmdlet
    //{
    //    protected override void BeginProcessing()
    //    {
    //        base.BeginProcessing();
    //    }
    //    protected override void ProcessRecord()
    //    {
    //        base.ProcessRecord();
    //    }
    //    protected override void EndProcessing()
    //    {
    //        base.EndProcessing();
    //    }
    //    protected override void StopProcessing()
    //    {
    //        base.StopProcessing();
    //    }
    //}


    public static class TableFormatter
    {

        // TODO:文字幅の計算方法がだめ
        // var l = Encoding.GetEncoding("UTF-8").GetByteCount("ほ");
        // 何かしらの方法で、実際に描画する幅を計算しないとダメ。
        public static string toFormatTable<TEntity>(this IEnumerable<TEntity> entities)
        {
            var t = typeof(TEntity);
            var sb = new StringBuilder();

            // Column Length
            List<int> columnLengthList = new List<int>();
            var rowLength = 0;
            var index = 0;
            foreach(var p in t.GetProperties())
            {
                var columnLength = p.Name.StringInfo().LengthInTextElements;
                columnLengthList.Add(columnLength);
                rowLength += columnLength + 1;
                index++;
            }
            rowLength++;
            foreach (var entity in entities)
            {
                var _rowLength = 0;
                index = 0;
                foreach(var p in t.GetProperties())
                {
                    var columnLength = TableFormatter.toString(p.GetValue(entity)).StringInfo().LengthInTextElements;
                    columnLengthList[index] = System.Math.Max(columnLengthList[index], columnLength);
                    _rowLength += columnLength + 1;
                    index++;
                }
                _rowLength++;
                rowLength = System.Math.Max(rowLength, _rowLength);
            }

            // Header border top
            sb.AppendLine("".PadLeft(rowLength, '-'));

            // Header
            index = 0;
            foreach(var p in t.GetProperties())
            {
                sb.Append("|");
                sb.Append(p.Name.PadLeft(columnLengthList[index]));
                index++;
            }
            sb.AppendLine("|");

            // header border bottom
            sb.AppendLine("".PadLeft(rowLength, '-'));

            // body
            foreach (var entity in entities)
            {
                index = 0;
                foreach(var p in t.GetProperties())
                {
                    sb.Append("|");
                    var s = TableFormatter.toString(p.GetValue(entity));
                    var l = s.StringInfo().LengthInTextElements;
                    
                    sb.Append("".PadLeft(columnLengthList[index] - l) + s);
                    index++;
                }
                sb.AppendLine("|");
            }

            // body footer border bottom
            sb.AppendLine("".PadLeft(rowLength, '-'));

            return sb.ToString();
        }

        public static System.Globalization.StringInfo StringInfo(this string s) {
            return new System.Globalization.StringInfo(s);
        }

        public static IEnumerable<string> TextElements(this string s) {
            var en = System.Globalization.StringInfo.GetTextElementEnumerator(s);

            while (en.MoveNext())
            {
                yield return en.GetTextElement();
            }
        }

        public static string toString(object value)
        {
            if (value == null)
            {
                return "NULL";
            } else
            {
                return value.ToString();
            }
        }

    }
    class PersonnelResult
    {
        public string employee { get; set; }
        public string child { get; set; }
    }
}
