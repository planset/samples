using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Web.Mvc;

namespace MVC_ClientValidation.Validation
{
    [AttributeUsage(AttributeTargets.Property, AllowMultiple = false)]
    public sealed class NotAllowAllUpperCaseAttribute : ValidationAttribute, IClientValidatable
    {
        public NotAllowAllUpperCaseAttribute()
        {
            Enable = true;
            ErrorMessage = "すべて大文字にすることはできません。";
        }

        public bool Enable { get; set; }

        public IEnumerable<ModelClientValidationRule> GetClientValidationRules(ModelMetadata metadata, ControllerContext context)
        {
            // ValidationType は JavaScript 側でも使う
            var rule = new ModelClientValidationRule
            {
                ValidationType = "notallowalluppercase",
                ErrorMessage = FormatErrorMessage(metadata.GetDisplayName()),
            };

            // 追加のパラメータが存在する場合はセット
            rule.ValidationParameters["enable"] = Enable;

            // 作成したルールを返す
            yield return rule;
        }

        public override bool IsValid(object value)
        {
            // null の場合には検証しない
            if (value == null)
            {
                return true;
            }

            var s = (string)value;

            // Enableがtrueかつ全て大文字なら検証失敗
            if (Enable && s.All(char.IsUpper))
            {
                return false;
            }

            return true;
        }
    }
}
