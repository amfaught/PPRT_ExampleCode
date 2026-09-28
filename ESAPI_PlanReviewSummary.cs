// PlanReviewSummary.cs - Eclipse single-file plugin (read-only).
// Run from Tools > Scripts with a plan open.
using System.Linq;
using System.Windows;
using System.Windows.Controls;
using VMS.TPS.Common.Model.API;

namespace VMS.TPS
{
    public class Script
    {
        public void Execute(ScriptContext context, Window window)
        {
            PlanSetup plan = context.PlanSetup;
            if (plan == null) { MessageBox.Show("Open a plan first."); return; }

            string image = (plan.StructureSet != null && plan.StructureSet.Image != null)
                ? plan.StructureSet.Image.Id : "(none)";

            var rows = new[]
            {
                new[] { "Patient Name:",   context.Patient.LastName + ", " + context.Patient.FirstName },
                new[] { "MRN:",            context.Patient.Id },
                new[] { "Plan:",           plan.Id },
                new[] { "Planning Image:", image },
                new[] { "Beam Names:",     string.Join(", ", plan.Beams.Where(b => !b.IsSetupField).Select(b => b.Id)) },
            };

            var grid = new Grid { Margin = new Thickness(15) };
            grid.ColumnDefinitions.Add(new ColumnDefinition { Width = GridLength.Auto });
            grid.ColumnDefinitions.Add(new ColumnDefinition());
            for (int i = 0; i < rows.Length; i++)
            {
                grid.RowDefinitions.Add(new RowDefinition());
                var label = new TextBlock { Text = rows[i][0], FontWeight = FontWeights.Bold, Margin = new Thickness(0, 5, 15, 5) };
                var value = new TextBlock { Text = rows[i][1], Margin = new Thickness(0, 5, 0, 5) };
                Grid.SetRow(label, i); Grid.SetRow(value, i); Grid.SetColumn(value, 1);
                grid.Children.Add(label); grid.Children.Add(value);
            }

            window.Title = "Plan Review Summary";
            window.Content = grid;
            window.SizeToContent = SizeToContent.WidthAndHeight;
        }
    }
}
